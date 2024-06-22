from bs4 import BeautifulSoup
import pathlib
import shutil
import streamlit as st

GA_ID = "google_analytics"
GA_SCRIPT = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-WZGPN73NKB"></script>
<script id='google_analytics'>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-WZGPN73NKB');
</script>
"""

def inject_ga():
    index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    print(f"Index path: {index_path}")

    if not index_path.exists():
        print(f"Index file does not exist: {index_path}")
        return

    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    current_html = soup.prettify()
    print(f"Current HTML: {current_html}")

    if not soup.find(id=GA_ID):
        print("GA script not found, injecting...")
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            print(f"Backup exists, restoring: {bck_index}")
            shutil.copy(bck_index, index_path)
        else:
            print(f"Creating backup: {bck_index}")
            shutil.copy(index_path, bck_index)
        new_html = str(soup).replace('<head>', '<head>\n' + GA_SCRIPT)
        print(f"Modified HTML: {new_html}")
        index_path.write_text(new_html)
    else:
        print("GA script already present, no need to inject.")

    confirmed_html = index_path.read_text()
    print(f"Confirmed HTML after injection: {confirmed_html}")

inject_ga()

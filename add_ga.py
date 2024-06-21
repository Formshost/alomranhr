from bs4 import BeautifulSoup
import pathlib
import shutil
import streamlit as st

GA_ID = "google_analytics"
GA_SCRIPT = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-WZGPN73NKB"></script>
<script id="google_analytics">
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-WZGPN73NKB');
</script>
"""

def inject_ga():
    index_path = pathlib.Path(__file__).parent / "static" / "index.html"
    print(f"Index path: {index_path}")
    
    if not index_path.exists():
        print("index.html does not exist")
        return
    
    soup = BeautifulSoup(index_path.read_text(), features="html.parser")
    
    if not soup.find(id=GA_ID):
        bck_index = index_path.with_suffix('.bck')
        if bck_index.exists():
            shutil.copy(bck_index, index_path)
        else:
            shutil.copy(index_path, bck_index)
        
        html = str(soup)
        print("Current HTML:", html)  # Print the current HTML content before modification
        
        new_html = html.replace('<head>', '<head>\n' + GA_SCRIPT)
        print("Modified HTML:", new_html)  # Print the modified HTML content
        
        index_path.write_text(new_html)
        print("GA script injected successfully")
    else:
        print("GA script already present")

inject_ga()

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
    if not index_path.exists():
        print("index.html does not exist")
        return
    
    print(f"Index path: {index_path}")
    with open(index_path, 'r') as file:
        content = file.read()
        print(f"Current HTML: {content}")
    
    soup = BeautifulSoup(content, 'html.parser')
    if not soup.find(id=GA_ID):
        backup_path = index_path.with_suffix('.bck')
        if backup_path.exists():
            shutil.copy(backup_path, index_path)
        else:
            shutil.copy(index_path, backup_path)
        
        head = soup.find('head')
        head.insert(0, BeautifulSoup(GA_SCRIPT, 'html.parser'))
        new_content = str(soup)
        print(f"Modified HTML: {new_content}")
        with open(index_path, 'w') as file:
            file.write(new_content)
        print("GA script injected successfully")
        with open(index_path, 'r') as file:
            confirmed_content = file.read()
            print(f"Confirmed HTML after injection: {confirmed_content}")
    else:
        print("GA script already present")

inject_ga()

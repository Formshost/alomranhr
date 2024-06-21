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
    
    html_content = index_path.read_text()
    soup = BeautifulSoup(html_content, features="html.parser")
    
    if not soup.find(id=GA_ID):
        bck_index = index_path.with_suffix('.bck')
        if not bck_index.exists():
            shutil.copy(index_path, bck_index)
        
        print("Current HTML:", html_content)  # Print the current HTML content before modification
        
        if soup.head:
            soup.head.insert(0, BeautifulSoup(GA_SCRIPT, features="html.parser"))
        else:
            soup.insert(0, BeautifulSoup(GA_SCRIPT, features="html.parser"))
            
        new_html = str(soup)
        
        print("Modified HTML:", new_html)  # Print the modified HTML content
        
        index_path.write_text(new_html)
        print("GA script injected successfully")
        
        # Read back the file to confirm the changes
        confirmed_html = index_path.read_text()
        print("Confirmed HTML after injection:", confirmed_html)  # Confirm the changes
    else:
        print("GA script already present")

inject_ga()

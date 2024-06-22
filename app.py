import streamlit as st
import pandas as pd
import joblib
import os
from model import predict, predict_proba  # Ensure these functions handle DataFrame input
import streamlit.components.v1 as components




# set the theme configuration
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="🧑‍💼",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Custom CSS to hide the "Fork" button, GitHub icon, and "Hosted with Streamlit" footer
hide_streamlit_style = """
    <style>
        .stApp header {display: none !important;}
        footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Google Analytics script
GA_SCRIPT = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-WZGPN73NKB"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-WZGPN73NKB');
</script>
"""

# Inject the Google Analytics script into the Streamlit app
components.html(GA_SCRIPT, height=0, width=0)

# Rest of your Streamlit app code
st.title('My Streamlit App')
# Add more Streamlit components as needed



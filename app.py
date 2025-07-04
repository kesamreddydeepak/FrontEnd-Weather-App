import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# Set up the page
st.set_page_config(page_title="Weather App", layout="centered")

# Title
st.title("🌤️ Weather App")

# Read the HTML, CSS, and JS
html = Path("index.html").read_text()
css = Path("style.css").read_text()
js = Path("script.js").read_text()

# Inject CSS and JS into HTML
html_full = f"""
<style>{css}</style>
{html}
<script>{js}</script>
"""

# Render the full app in an iframe
components.html(html_full, height=700, scrolling=True)

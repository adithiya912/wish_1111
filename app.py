import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="11:11 — A tiny wish", page_icon="💗", layout="wide")
html = Path(__file__).with_name("site.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)

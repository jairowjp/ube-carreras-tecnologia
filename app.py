"""Sitio de promoción de las carreras de tecnología de la UBE, servido con Streamlit."""
import base64
import pathlib

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Carreras de tecnología · UBE",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Oculta la interfaz de Streamlit para que la página ocupe toda la pantalla
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden; height: 0;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      iframe {display: block; height: 100vh !important; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

BASE = pathlib.Path(__file__).parent
html = (BASE / "index.html").read_text(encoding="utf-8")

# Si existe un logo en assets/, se inserta en la cabecera en lugar del marcador "UBE"
LOGOS = (("logo.png", "image/png"), ("logo.svg", "image/svg+xml"), ("logo.jpg", "image/jpeg"), ("logo.webp", "image/webp"))
for name, mime in LOGOS:
    path = BASE / "assets" / name
    if path.exists():
        b64 = base64.b64encode(path.read_bytes()).decode()
        start, end = "<!--LOGO_START-->", "<!--LOGO_END-->"
        i, j = html.index(start), html.index(end) + len(end)
        html = html[:i] + f'<img src="data:{mime};base64,{b64}" alt="Universidad Bolivariana del Ecuador">' + html[j:]
        break

components.html(html, height=900, scrolling=True)

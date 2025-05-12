import streamlit as st
from utils.auth import login
from utils.process import process_files

st.set_page_config(
    page_title="RMR | Comparador de Cotações",
    layout="wide",
    page_icon="🔧"
)

# Estilização customizada
def local_css():
    st.markdown("""
        <style>
            .main {
                background-color: #f5f7fa;
            }
            header, .css-1q7yb06 {
                background-color: #1c1c1c;
                color: white;
            }
            .block-container {
                padding: 2rem 3rem;
            }
            h1, h2, h3, h4 {
                color: #003366;
            }
            .stButton>button {
                background-color: #003366;
                color: white;
                border: none;
                padding: 0.6em 1.2em;
                border-radius: 8px;
            }
            .stDownloadButton>button {
                background-color: #0077b6;
                color: white;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

local_css()

if login():
    st.image(r"C:\Users\sitet\OneDrive\Área de Trabalho\ComparadorRMR\assets\logo.png", width=250)
    st.title("🔧 Comparador de Cotações RMR")
    st.markdown("Envie suas planilhas e obtenha rapidamente os melhores preços por peça.")
    process_files()

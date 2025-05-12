import streamlit as st
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

def login():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        return True

    st.sidebar.image("assets/logo-rmr.png", width=250)
    st.sidebar.title("🔐 Login")

    with st.sidebar.form("login_form"):
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar")

    if submitted:
        if username == os.getenv("USERNAME") and password == os.getenv("SENHA"):
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.sidebar.error("Credenciais inválidas.")

    return False

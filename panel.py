import streamlit as st
import os

st.set_page_config(page_title="Admin Panel – IRCLASS Payroll", layout="wide")
st.title("🔐 Admin Panel – Upload New Policy")

password = st.text_input("Enter Admin Password", type="password")
if password != "admin2025":
    st.warning("Enter valid admin password to proceed.")
    st.stop()

uploaded_file = st.file_uploader("📄 Upload Updated Policy PDF", type=["pdf"])
if uploaded_file:
    file_path = os.path.join("vectorstore", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"✅ Uploaded and saved: {uploaded_file.name}")
    st.info("Chatbot will now reference this policy document as well.")

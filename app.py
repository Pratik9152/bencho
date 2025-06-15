import streamlit as st
from utils import get_answer

st.set_page_config(
    page_title="IRCLASS Payroll Chatbot",
    layout="wide",
    page_icon="🤖"
)

st.markdown("""
<style>
body {
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.stApp {
    background: linear-gradient(120deg, #0f2027, #203a43, #2c5364);
    color: white;
}
.title h1, .markdown-text-container h1, .markdown-text-container h2, .markdown-text-container h3 {
    color: #00ffd5;
}
.block-container {
    padding: 2rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 IRCLASS Payroll Chatbot")
st.markdown("Ask payroll-related questions in English, Hindi, Tamil, Kannada, Bengali.")
st.markdown("---")

query = st.text_input("💬 Enter your payroll question:")

if query:
    with st.spinner("🔍 Fetching answer..."):
        answer = get_answer(query)
        st.markdown("### 📌 Answer:")
        st.markdown(answer, unsafe_allow_html=True)

st.markdown("---")
st.subheader("📄 About Us")

try:
    with open("about_us.md", "r", encoding="utf-8") as f:
        st.markdown(f.read())
except FileNotFoundError:
    st.warning("About Us file not found.")

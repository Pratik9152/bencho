import streamlit as st
from utils import get_answer
import time

st.set_page_config(
    page_title="IRCLASS Payroll Chatbot",
    layout="wide",
    page_icon="🤖"
)

st.markdown("""
<style>
body {
    background-color: #121212;
    color: #eaeaea;
}
.stApp {
    background-color: #121212;
    color: #eaeaea;
}
.title h1, .markdown-text-container h1, .markdown-text-container h2, .markdown-text-container h3 {
    color: #00ffd5;
}
.block-container {
    padding: 2rem;
}
.bot-message {
    background-color: #1f1f1f;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
}
.user-message {
    background-color: #3a3a3a;
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 IRCLASS Payroll Chatbot")
st.markdown("Ask payroll-related questions in English, Hindi, Tamil, Kannada, Bengali.")
st.markdown("---")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("💬 Type your payroll question:")

if query:
    st.session_state.chat_history.append(("user", query))
    with st.spinner("🤖 Typing response..."):
        answer = get_answer(query)
        st.session_state.chat_history.append(("bot", answer))

# Render chat history
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"<div class='user-message'><strong>🧑 You:</strong><br>{message}</div>", unsafe_allow_html=True)
    else:
        with st.empty():
            display_text = ""
            for char in message:
                display_text += char
                time.sleep(0.01)
                st.markdown(f"<div class='bot-message'><strong>🤖 IRCLASS Bot:</strong><br>{display_text}</div>", unsafe_allow_html=True)

st.markdown("---")
st.subheader("📄 About Us")
try:
    with open("about_us.md", "r", encoding="utf-8") as f:
        st.markdown(f.read())
except FileNotFoundError:
    st.warning("About Us file not found.")

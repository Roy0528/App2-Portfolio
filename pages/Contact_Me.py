import streamlit as st

st.set_page_config(layout="wide")

st.header("聯絡我 Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("您的信箱")
    message = st.text_area("您想詢問的問題")
    button = st.form_submit_button(label="提交")
    if button:
        pass
        
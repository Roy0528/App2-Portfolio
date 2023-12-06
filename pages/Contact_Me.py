import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")

st.header("聯絡我 Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("您的信箱")
    raw_message = st.text_area("您想詢問的問題")
    message = f"""\
Subject: New email from {user_email}
From: {user_email}
{raw_message}
"""
    button = st.form_submit_button(label="提交")
    if button:
        send_email(message)
        st.info("成功寄出信件！")
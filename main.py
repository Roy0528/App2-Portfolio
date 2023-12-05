import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("吳泓儒")
    content = """
    嗨，我畢業於國立臺灣大學心理學研究所－工商組，熱衷於學習與人力資源有關的技能，包含招募任用、訓練發展等。
    在學期間除了曾經擔任校內助教與研究助理外，亦參與過產學合作專案（國內房仲產業專案管理助理），同時也曾經協助舉辦組織行為工作坊。
    關於學校課程方面，除了進修專業課程外，因為對於程式語言有著一定的熱誠（Python、SQL、R語言），
    也曾經修過大數據商業分析以及商管程式設計，期望透過程式語言探索組織內各式各樣與人力資源有關的議題。
    曾擔任系上排球隊隊長，帶領團隊獲得良好成績，對於任務是否可以圓滿達成有一定的堅持，是一位負責任、並能確實達成任務目標的問題執行者。
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
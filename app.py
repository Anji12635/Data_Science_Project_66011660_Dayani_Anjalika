import streamlit as st
import pandas as pd
import ast

st.set_page_config(page_title="BERTopic Dashboard", layout="wide")

st.markdown("""
<style>
.stApp { background-color: white; }
.topic-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #f7f7f7;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Top 10 BERTopic Topics")

df = pd.read_csv("top10_topics.csv")
df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)

for i, row in df.iterrows():
    try:
        words = ast.literal_eval(row["Representation"])
        keywords = ", ".join(words[:5])
    except:
        keywords = row["Representation"]

    st.markdown(f"""
    <div class="topic-box">
        <h3>Topic {i+1}</h3>
        <p><b>Keywords:</b> {keywords}</p>
        <p><b>Mentions:</b> {row['Count']}</p>
    </div>
    """, unsafe_allow_html=True)

st.bar_chart(df["Count"])

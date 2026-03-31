import streamlit as st
import pandas as pd
import ast

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="BERTopic Dashboard", layout="wide")

# -------------------------------
# Styling
# -------------------------------
st.markdown("""
<style>
.stApp { background-color: white; }

.topic-box {
    padding: 20px;
    border-radius: 12px;
    background-color: #f7f7f7;
    margin-bottom: 15px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("📊 Top 10 BERTopic Topics")

# -------------------------------
# Load CSV
# -------------------------------
df = pd.read_csv("top10_topics.csv")
df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)

# -------------------------------
# Display Topics
# -------------------------------
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

# -------------------------------
# Bar Chart
# -------------------------------
st.subheader("📈 Topic Distribution")
st.bar_chart(df["Count"])

# -------------------------------
# Topic Map (HTML version)
# -------------------------------
st.markdown("---")
st.subheader("🧠 Interactive Topic Map")

try:
    with open("topics.html", "r", encoding="utf-8") as f:
        html = f.read()

    st.components.v1.html(html, height=800, scrolling=True)

except FileNotFoundError:
    st.error("⚠️ topics.html not found. Please upload it.")

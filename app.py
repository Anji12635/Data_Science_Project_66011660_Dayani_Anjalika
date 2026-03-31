import streamlit as st
import pandas as pd
import ast
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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
# Topic Cards
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
# Word Cloud Section
# -------------------------------
st.markdown("---")
st.subheader("☁️ Topic Word Clouds")

def generate_wordcloud(words):
    text = " ".join(words)
    wc = WordCloud(
        width=400,
        height=250,
        background_color="white",
        colormap="tab10"
    ).generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation="bilinear")
    ax.axis("off")
    return fig

# Grid layout (2 columns)
cols = st.columns(2)

for i, row in df.iterrows():
    try:
        words = ast.literal_eval(row["Representation"])
    except:
        words = [row["Representation"]]

    with cols[i % 2]:
        st.markdown(f"### Topic {i+1}")
        fig = generate_wordcloud(words)
        st.pyplot(fig)

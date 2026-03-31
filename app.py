import streamlit as st
import pandas as pd
import ast
from bertopic import BERTopic

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="BERTopic Dashboard", layout="wide")

# -------------------------------
# Custom Styling
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

h3 {
    margin-bottom: 5px;
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
# Load BERTopic Model (cached)
# -------------------------------
@st.cache_resource
def load_model():
    return BERTopic.load("my_model")  # ⚠️ change path if needed

# -------------------------------
# BERTopic Visualization
# -------------------------------
st.markdown("---")
st.subheader("🧠 Interactive Topic Map")

model = load_model()

if st.button("Show Topic Map"):
    fig = model.visualize_topics()
    st.plotly_chart(fig, use_container_width=True)

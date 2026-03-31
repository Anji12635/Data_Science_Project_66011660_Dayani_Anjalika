import streamlit as st
import pandas as pd
import ast

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(page_title="Topic Dashboard", layout="wide")

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
    margin-bottom: 20px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}

.review-box {
    padding: 10px;
    border-left: 5px solid #4D96FF;
    margin-bottom: 10px;
    background-color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Title
# -------------------------------
st.title("📊 Top 10 Topics + Reviews")

# -------------------------------
# Load CSV
# -------------------------------
df = pd.read_csv("top10_topics.csv")
df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)

# -------------------------------
# Display Topics
# -------------------------------
for i, row in df.iterrows():

    # Keywords
    try:
        words = ast.literal_eval(row["Representation"])
        keywords = ", ".join(words[:5])
    except:
        keywords = row["Representation"]

    # Representative docs (reviews)
    try:
        reviews = ast.literal_eval(row["Representative Docs"])
    except:
        reviews = [row["Representative Docs"]]

    st.markdown(f"""
    <div class="topic-box">
        <h3>Topic {row['Topic']}</h3>
        <p><b>Keywords:</b> {keywords}</p>
        <p><b>Mentions:</b> {row['Count']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Show top reviews
    st.markdown("**Top Reviews:**")

    for r in reviews[:3]:  # show top 3 reviews
        st.markdown(f"""
        <div class="review-box">
            {r}
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# Bar chart
# -------------------------------
st.subheader("📈 Topic Distribution")
st.bar_chart(df["Count"])

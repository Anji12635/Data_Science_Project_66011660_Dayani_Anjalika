import streamlit as st
import pandas as pd
import ast

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

st.title("📊 Topics & Reviews Dashboard")

# -------------------------------
# Load data
# -------------------------------
df = pd.read_csv("top10_topics.csv")
df = df.sort_values(by="Count", ascending=False).reset_index(drop=True)

# -------------------------------
# Display
# -------------------------------
for i, row in df.iterrows():

    # ✅ Keywords
    try:
        words = ast.literal_eval(row["Representation"])
        keywords = ", ".join(words[:5])
    except:
        keywords = row["Representation"]

    # ✅ Reviews
    try:
        reviews = ast.literal_eval(row["Representative_Docs"])
    except:
        reviews = [row["Representative_Docs"]]

    # Topic card
    st.markdown(f"""
    <div class="topic-box">
        <h3>Topic {row['Topic']}</h3>
        <p><b>Keywords:</b> {keywords}</p>
        <p><b>Mentions:</b> {row['Count']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Reviews
    st.markdown("**Top Reviews:**")

    for r in reviews[:3]:
        st.markdown(f"""
        <div class="review-box">
            {r}
        </div>
        """, unsafe_allow_html=True)

# -------------------------------
# Chart
# -------------------------------
st.subheader("📈 Topic Distribution")
st.bar_chart(df["Count"])

import streamlit as st

from utils import extract_text

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:
    text = extract_text(uploaded_file)

    st.success("Resume uploaded successfully!")

    st.text_area(
        "Extracted Text",
        text,
        height=300
    )
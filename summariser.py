import streamlit as st
from summarizer import Summarizer
st.title("Extractive Summarizer")
st.sidebar.title("Options")
summarization_mode = st.sidebar.radio(
    "Summarize by:",
    ("Ratio of text", "Number of sentences")
)
st.header("Input Text")
body = st.text_area("Paste your text below", height=400)
model = Summarizer()
if summarization_mode == "Ratio of text":
    summary_ratio = st.sidebar.slider("Select summary ratio (e.g., 0.2 = 20%)", min_value=0.2, max_value=0.9, value=0.2, step=0.05)
    sentence_limit = None  
elif summarization_mode == "Number of sentences":
    sentence_limit = st.sidebar.number_input("Limit number of sentences", min_value=3, max_value=20, value=5, step=1)
    summary_ratio = None  

if body:
    st.subheader("Original Text")
    st.write(body)  

    word_count_input = len(body.split())
    st.write(f"Word Count (Input): {word_count_input}")
    if summarization_mode == "Ratio of text" and summary_ratio:
        summary = model(body, ratio=summary_ratio)
    elif summarization_mode == "Number of sentences" and sentence_limit:
        summary = model(body)
        summary_sentences = summary.split('.')
        summary = '.'.join(summary_sentences) 
    st.subheader("Summarized Text")
    st.write(summary)
    word_count_summary = len(summary.split())
    st.write(f"Word Count (Summary): {word_count_summary}")
    reduction_percentage = ((word_count_input - word_count_summary) / word_count_input) * 100
    st.write(f"Text Reduction: {reduction_percentage:.2f}%")

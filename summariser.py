import streamlit as st
from summarizer import Summarizer
def summarize_file(body):
    
    model = Summarizer()
    
    if body:
        #st.subheader("Original Text")
        #st.write(body)  

        word_count_input = len(body.split())
        st.write(f"Word Count (Input): {word_count_input}")
        summary = model(body, ratio=0.4)
        return summary
    
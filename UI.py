import streamlit as st

def app():
    st.title("Simple PDF Text Extractor")
    
    st.markdown("""
    ### Instructions:
    1. Upload a PDF file to extract text from it.
    2. Click the 'Extract Text' button to see the content.
    """)

    # File uploader (no functionality attached yet)
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    # Button to trigger text extraction (no functionality yet)
    if st.button("Extract Text"):
        st.write("Text will be extracted and displayed here.")

    # Placeholder for displaying extracted text
    st.text_area("Extracted Text", "", height=200)

    # Footer or additional info
    st.markdown("""
    **Note:** This is a simple UI demonstration. No text extraction functionality is currently implemented.
    """)

if __name__ == "__main__":
    app()

import streamlit as st
import freq_based_ranking
import webbrowser
import os

st.title("PDF Keyword Search Tool")

# Step 1: Text Extraction

# Text input for folder path
folder_path = st.text_input("Enter the folder path containing PDF documents:")

# Initialize session state to store extracted texts and search results
if "pdf_texts" not in st.session_state:
    st.session_state["pdf_texts"] = None
if "search_results" not in st.session_state:
    st.session_state["search_results"] = None

# Button to process and extract text from PDFs
if st.button('Process PDFs'):
    if folder_path:
        folder_paths = [folder_path]
        with st.spinner("Extracting text from PDFs..."):
            # Extract the text from PDFs
            pdf_texts = freq_based_ranking.extract_pdf_text(folder_paths)
            st.session_state["pdf_texts"] = pdf_texts
            st.success("Text extraction completed!")
    else:
        st.error("Please enter a valid folder path.")

# Step 2: Keyword Search

# Text input for keyword
keyword = st.text_input("Enter the keyword to search for:")

# Submit button to trigger keyword search
if st.button('Submit'):
    if st.session_state["pdf_texts"] and keyword:
        with st.spinner("Searching for keyword..."):
            search_results = freq_based_ranking.search_in_pdf_texts(st.session_state["pdf_texts"], keyword)
            st.session_state["search_results"] = search_results

            if search_results:
                st.success("Search completed!")
            else:
                st.warning("No results found.")
    else:
        st.error("Please process PDFs and enter a keyword before searching.")

# Step 3: Display Results

# If we have search results, display them
if st.session_state["search_results"]:
    ranked_results = st.session_state["search_results"]

    # Display each result with a button to open the corresponding PDF
    for file_path, score in ranked_results.items():
        if score > 0:
            # Create two columns, one for the text and one for the progress bar
            col1, col2 = st.columns([3, 1])

            with col1:
                # Show the file name and occurrence count
                st.write(f"**{os.path.basename(file_path)}** - Occurrences: {score}")
            
            with col2:
                # Display a progress bar for keyword occurrence
                max_score = max(ranked_results.values())
                st.progress(min(100, int((score / max_score) * 100)))

            # Create buttons: Open File, Summarize, Tap to Hear
            col_button1, col_button2, col_button3 = st.columns([1, 1, 1])

            # Open File button
            with col_button1:
                if st.button(f"Open File", key=f"open_{os.path.basename(file_path)}"):
                    if os.path.exists(file_path):
                        webbrowser.open('file://' + os.path.realpath(file_path))
                    else:
                        st.error(f"File {file_path} not found.")

            # Summarize button (placeholder for your summarizer function)
            with col_button2:
                if st.button("Summarize", key=f"summarize_{os.path.basename(file_path)}"):
                    #st.write(f"Summarizing content from {os.path.basename(file_path)}...")
                    st.write(st.session_state["pdf_texts"][file_path])
                    # summary = summariser.summarize_file(file_path)  # Implement your summarizer here
                    # st.write(summary)

            # Tap to Hear button (placeholder for your text-to-speech function)
            with col_button3:
                if st.button("Tap to Hear", key=f"hear_{os.path.basename(file_path)}"):
                    st.write(f"Playing audio for {os.path.basename(file_path)}...")
                    # freq_based_ranking.text_to_speech(file_path)  # Implement your text-to-speech function
            st.divider()

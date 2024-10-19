import streamlit as st
import freq_based_ranking
import summariser
import os
import shutil
import atexit  # To handle cleanup at the end of the program
from audio import audio, stop_audio  

# Create temp_audio directory if it doesn't exist
if not os.path.exists('temp_audio'):
    os.makedirs('temp_audio')

st.title("PDF Keyword Search and Text-to-Speech Tool")

# Step 1: Text Extraction
folder_path = st.text_input("Enter the folder path containing PDF documents:")

# Initialize session state to store extracted texts, search results, summaries, and audio paths
if "pdf_texts" not in st.session_state:
    st.session_state["pdf_texts"] = None
if "search_results" not in st.session_state:
    st.session_state["search_results"] = None
if "summaries" not in st.session_state:
    st.session_state["summaries"] = {}
if "audio_paths" not in st.session_state:
    st.session_state["audio_paths"] = {}

# Button to process and extract text from PDFs
if st.button('Process PDFs'):
    if folder_path:
        folder_paths = [folder_path]
        with st.spinner("Extracting text from PDFs..."):
            pdf_texts = freq_based_ranking.extract_pdf_text(folder_paths)
            st.session_state["pdf_texts"] = pdf_texts
            st.success("Text extraction completed!")
    else:
        st.error("Please enter a valid folder path.")

# Step 2: Keyword Search
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

# Step 3: Display Results and Integrate Text-to-Speech
if st.session_state["search_results"]:
    ranked_results = st.session_state["search_results"]
    count = 0

    for file_path, score in ranked_results.items():
        count += 1
        if score > 0:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**{os.path.basename(file_path)}** - Occurrences: {score}")
            
            with col2:
                max_score = max(ranked_results.values())
                st.progress(min(100, int((score / max_score) * 100)))

            # Create buttons for "Open File" and "Summarize"
            col_button1, col_button2 = st.columns([1, 1])

            # Open File button
            with col_button1:
                if st.button(f"Open File: {os.path.basename(file_path)}", key=f"open_{count}"):
                    freq_based_ranking.open_file(file_path)

            # Summarize button
            summary = None
            with col_button2:
                if st.button("Summarize", key=f"summarize_{count}"):
                    # Check if the summary already exists in session_state
                    if file_path not in st.session_state["summaries"]:
                        summary = summariser.summarize_file(st.session_state["pdf_texts"][file_path][0])
                        st.session_state["summaries"][file_path] = summary
                    else:
                        summary = st.session_state["summaries"][file_path]

            # Display the summary (if any) in an expander
            if file_path in st.session_state["summaries"]:
                with st.expander(f"Summary of {os.path.basename(file_path)}", expanded=True):
                    st.write(st.session_state["summaries"][file_path])

                    # Add Tap to Hear button within the expander for summarized content
                    if st.button("Tap to Hear", key=f"hear_summary_{count}"):
                        # Create a unique path for the audio file in a temporary directory
                        audio_file_path = os.path.join('temp_audio', f"summary_audio_{count}.wav")
                        # Generate audio for the summarized content
                        audio(st.session_state["summaries"][file_path], audio_file_path)
                        # Store the audio path in session_state
                        st.session_state["audio_paths"][file_path] = audio_file_path

                    # Display audio player if the file was generated
                    if file_path in st.session_state["audio_paths"]:
                        audio_path = st.session_state["audio_paths"][file_path]
                        if os.path.exists(audio_path):
                            st.audio(audio_path)
                        else:
                            st.error(f"Audio file not found: {audio_path}")

            st.divider()

# Cleanup function to delete temp_audio files after the program ends
def cleanup_temp_audio():
    if os.path.exists('temp_audio'):
        shutil.rmtree('temp_audio')

# Register cleanup function to run at exit
atexit.register(cleanup_temp_audio)

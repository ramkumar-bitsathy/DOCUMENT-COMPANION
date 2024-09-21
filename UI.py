import streamlit as st
import os
import numpy as np
import freq_based_ranking
import summariser
import webbrowser  # Import webbrowser to open the file

st.title("PDF Keyword Search Tool")

# Text input for folder path and keyword
folder_path = st.text_input("Enter the folder path containing PDF documents:")
keyword = st.text_input("Enter the keyword to search for:")

# Initialize session state to store search results
if "search_results" not in st.session_state:
    st.session_state["search_results"] = None

# Submit button to trigger search
if st.button('Submit'):
    with st.spinner("Fetching in process"):
        if folder_path and keyword:
            folder_paths = [folder_path]

            # Search for files using your custom function
            search_results = freq_based_ranking.search_files(folder_paths, keyword)
            st.session_state["search_results"] = search_results  # Save results in session state

            if search_results:
                st.success("Search completed!")
            else:
                st.warning("No results found.")

        else:
            st.error("Please enter both folder path and keyword.")

# If we have search results, display them
if st.session_state["search_results"]:
    search_results = st.session_state["search_results"]
    keys = list(search_results.keys())
    values = list(search_results.values())

    # Sort the results based on the frequency of the keyword
    sorted_value_index = np.argsort(values)
    ranked_results = {keys[i]: values[i] for i in sorted_value_index[::-1]}

    # Display each result with a button to open the corresponding PDF
    for file_path, score in ranked_results.items():
        if score > 0:
            # Create two columns, one for the text and one for the half-sized progress bar
            col1, col2 = st.columns([3, 1])  # Adjust column widths as needed

            with col1:
                # Show the file name and occurrence count
                st.write(f"**{file_path[1]}** occurrence: {score}")
            
            with col2:
                # Display a smaller progress bar for keyword occurrence
                st.progress(min(100, int((score / max(ranked_results.values())) * 100)))

            # Create a row of 3 buttons: Open File, Summarize, and Tap to Hear
            col_button1, col_button2, col_button3 = st.columns([1, 1, 1])

            # Add "Open File" button with a unique key
            with col_button1:
                if st.button(f"Open File", key=f"open_{file_path[1]}"):
                    pdf_file_path = file_path[0]  # Get the actual file path
                    if os.path.exists(pdf_file_path):
                        # Open the file using the default PDF viewer
                        webbrowser.open('file://' + os.path.realpath(pdf_file_path))
                    else:
                        st.error(f"File {pdf_file_path} not found.")

            # Add "Summarize" button
            
            with col_button2:
                if st.button("Summarize", key=f"summarize_{file_path[1]}"):
                    # Call a hypothetical summarize function (replace with actual logic)
                    st.write(f"Summarizing content from {file_path[1]}...")
                    summary = summariser.summarize_file(file_path[0])
                    st.write(summary)

            # Add "Tap to Hear" button
            with col_button3:
                if st.button("Tap to Hear", key=f"hear_{file_path[1]}"):
                    # Call a hypothetical text-to-speech function (replace with actual logic)
                    st.write(f"Playing audio for {file_path[1]}...")
                    freq_based_ranking.text_to_speech(file_path[0])
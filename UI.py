import streamlit as st
import os
import numpy as np
import freq_based_ranking


st.title("PDF Keyword Search Tool")

folder_path = st.text_input("Enter the folder path containing PDF documents:")
keyword = st.text_input("Enter the keyword to search for:")


if st.button('Submit'):
    with st.spinner("Fetching in process"):
        if folder_path and keyword:
            folder_paths = [folder_path]

            search_results = freq_based_ranking.search_files(folder_paths, keyword)
            st.write(search_results)

            if search_results:
                keys = list(search_results.keys())
                values = list(search_results.values())
                #sorting is made here..
                sorted_value_index = np.argsort(values)
                ranked_results = {keys[i]: values[i] for i in sorted_value_index[::-1]}
  
                
                for file_path, score in ranked_results.items():
                    if score>0:
                        st.write(f"**{file_path[1]}** occurance:{score}")
                        # progress bar
                        st.progress(min(100, int((score / max(ranked_results.values())) * 100)))
                        st.button(
                            label=f"Open File: {file_path[1]}",
                            on_click=freq_based_ranking.open_file,
                            args=(file_path[0],),
                        )
                        # Add a button to open the PDF
                        
            else:
                st.write("No results found.")
        else:
            st.error("Please enter both folder path and keyword.")
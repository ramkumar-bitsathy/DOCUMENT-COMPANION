import os
from PyPDF2 import PdfFileReader
import numpy as np

def search_files(folder_paths, keyword):
    search_results = {}
    ranking = {}
    
    for folder_path in folder_paths:
        results = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".pdf"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, "rb") as f:
                            pdf = PdfFileReader(f)
                            frequency = 0
                            for page_num in range(pdf.getNumPages()):
                                page = pdf.getPage(page_num)
                                page_text = page.extractText()
                                
                                # Count occurrences of the keyword
                                if page_text and keyword.lower() in page_text.lower():
                                    frequency += page_text.lower().count(keyword.lower())
                                    results.append((file_path, file, page_num + 1))
                            ranking[file] = frequency
                    except Exception as e:
                        print(f"Error reading {file_path}: {e}")

        if results:
            search_results[folder_path] = results

    return ranking

def open_file(file_path):
    os.startfile(file_path)

# Specify the folder paths where your PDF documents are located
folder_paths = [r"C:\Users\RAMKUMAR K\Desktop\S5-MiniProject\test"]

# The keyword to search for in the PDF files
keyword = "virus"
search_results = search_files(folder_paths, keyword)

print("Search Results (Frequency):", search_results)

# Prepare ranking based on frequency of keyword occurrences
keys = list(search_results.keys())
values = list(search_results.values())

# Handle cases where no results were found
if values:
    sorted_value_index = np.argsort(values)
    ranked_results = {keys[i]: values[i] for i in sorted_value_index[::-1]}
    print(f"\nRanked Results:\n{ranked_results}")
else:
    print("No results found.")

# Uncomment below to print details about found results
"""
if len(search_results) > 0:
    for folder_path, results in search_results.items():
        print(f"Folder: {folder_path}")
        for result in results:
            file_path, file_name, page_num = result
            print(f"Found in File: {file_name}, Page: {page_num}")
            # open_file(file_path)
else:
    print("No results found.")
"""

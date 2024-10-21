import os
from PyPDF2 import PdfFileReader

def search_files(folder_paths, keyword):
    search_results = {}

    for folder_path in folder_paths:
        results = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".pdf"):
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as f:
                        pdf = PdfFileReader(f)
                        for page_num in range(pdf.getNumPages()):
                            page = pdf.getPage(page_num)
                            page_text = page.extractText()
                            
                            if keyword.lower() in page_text.lower():
                                results.append((file_path, file, page_num + 1))
                                print(result)

        if results:
            search_results[folder_path] = results

    return search_results

def open_file(file_path):
    os.startfile(file_path)

folder_paths = [r"C:\Users\RAMKUMAR K\Desktop\DR\local_drive_2", r"C:\Users\RAMKUMAR K\Desktop\DR\downloads"]

keyword = "electron"
search_results = search_files(folder_paths, keyword)

if len(search_results) > 0:
    for folder_path, results in search_results.items():
        print(f"Folder: {folder_path}")
        for result in results:
            file_path, file_name, page_num = result
            print(f"Found in File: {file_name}, Page: {page_num}")
            #open_file(file_path)
else:
    print("No results found.")
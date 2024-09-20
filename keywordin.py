from PyPDF2 import PdfFileReader

def extract_text_from_file(file_path):
    with open(file_path, "rb") as f:
        pdf = PdfFileReader(f)
        text = ""
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            text += page.extractText()
    return text

file_path = r"C:\Users\RAMKUMAR K\Desktop\S5-MiniProject\test\jmir-2006-2-e9.pdf"
text = extract_text_from_file(file_path)
print(text)

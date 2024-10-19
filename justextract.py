from PyPDF2 import PdfFileReader

def extract_text_from_file(file_path):
    with open(file_path, "rb") as f:
        pdf = PdfFileReader(f)
        text = ""
        for page_num in range(pdf.getNumPages()):
            page = pdf.getPage(page_num)
            text += page.extractText()
    return text


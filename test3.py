import PyPDF2  # This library is to read the PDF file

path = open('clean_ACM_DANCE_2015_FINAL.pdf', 'rb')

pdfReader = PyPDF2.PdfReader(path)
from_page = pdfReader.pages[2]

text = from_page.extract_text()
print(text)
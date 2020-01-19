from PyPDF2 import PdfFileReader
import os

pdfin = PdfFileReader(open('1.pdf', 'rb'), strict=False)

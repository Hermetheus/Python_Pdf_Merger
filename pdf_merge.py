from PyPDF2 import PdfFileMerger
import os


path = "/Users/allan/pdfmerger/"
pdf_files = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf']
merger = PdfFileMerger(strict=False)
for files in pdf_files:
    merger.append(path+files)
if not os.path.exists(path+'merged.pdf'):
    merger.write(path+'merged.pdf')
merger.close()

import PyPDF2
from PyPDF2 import PdfFileMerger
import os
import sys


# This is a pdf merger built using python. Beware that it only works with windows OS.

path = input("enter filepath like so eg C:\\Users\\sam\\Documents\\pdf\\: ")
pdf_name= input("name merged file with format 'name.pdf': ")
pdf_files = []
merger = PdfFileMerger()
for filename in os.listdir(path):
	pdf_files.append(filename)
	for files in pdf_files:
		merger.append(path+files, import_bookmarks=False)
		print("merge complete")
if not os.path.exists(path + pdf_name):
	merger.write(path+pdf_name)
merger.close()

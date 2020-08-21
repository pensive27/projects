import fitz
import os

# This is a pdf parser built using python. Beware that it only works with windows OS.

try:
    path = input("enter filepath like so eg C:\\Users\\sam\\Documents\\pdf\\: ")
except RuntimeError:
    print("invalid filepath")


file_to_open = path + input("name file name with format 'name.pdf': ")

search_term = input("Enter search term here: ").lower()

pdf_document = fitz.open(file_to_open)

try:
    for current_page in range(len(pdf_document)):
        page = pdf_document.loadPage(current_page)
        if page.searchFor(search_term):
            print("%s found on page %i" % (search_term.lower(), current_page +1))
            pages = pdf_document.loadPage(current_page)
            pagetext = pages.getText("text")
            print(pagetext)
except:
    print("File not found")

while True:
    user_input =input("Enter quit to end: ")
    if user_input == "quit":
        break





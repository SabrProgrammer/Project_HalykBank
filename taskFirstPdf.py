# Task first pdf
# Reading data from a Python PDF file - take an electronic document in PDF format and subtract data through python

# install the package use command
# pip3 install PyPDF2

# install pyDF2

from PyPDF2 import PdfFileReader

# file for reading
pdf_document = "File_For_Reading_PDF.pdf"

with open(pdf_document, "rb") as filehandle:
   pdf = PdfFileReader(filehandle)
   info = pdf.getDocumentInfo()
   pages = pdf.getNumPages()

   # info pdf
   print()
   print("Info:")
   print()
   print (info)

   # choose number of pages
   print()
   print ("number of pages: %i" % pages)
   print()

   # content of page
   number = int(input("Enter the number of the page:"))
   page = pdf.getPage(number)
   print(page)
   print(page.extractText())
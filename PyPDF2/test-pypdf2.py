import PyPDF2 as pp


paper = pp.PdfReader("aps.72.20230092.pdf")
print(paper.pages[0])
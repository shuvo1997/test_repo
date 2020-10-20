import PyPDF2

pdffileObj = open('NaBolteShikun.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdffileObj)
pdfReader.numPages
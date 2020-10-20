import PyPDF2
import pdfplumber
import io
import docx2txt

my_text = docx2txt.process("Bangla_word-list.doc")
print(my_text)


# s = ''
# with pdfplumber.open('NaBolteShikun.pdf') as pdf:
#     first_page = pdf.pages[5]
#     print(first_page.extract_text())
#     s = first_page.extract_text()

# with io.open('Banglatext.txt','w',encoding='utf-8') as f:
#     f.write(s)

# pdffileObj = open('First_Java.pdf','rb')
# pdfReader = PyPDF2.PdfFileReader(pdffileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(10)
# print(pageObj.extractText())
# file = open('textfile.txt','w')
# file.write(pageObj.extractText())
# file.close()

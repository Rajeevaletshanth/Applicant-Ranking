#Convert PDF to TXT
'''
import PyPDF2
pdffileobj = open('se resume.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(pdffileobj)
x = pdfreader.numPages
pageobj = pdfreader.getPage(x-1)
text=pageobj.extractText()


with open("Resume.txt", 'w') as fp:
	pass

file1 = open("Resume.txt", "a")
file1.writelines(text)
file1.close()
'''
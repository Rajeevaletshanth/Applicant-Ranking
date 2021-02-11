import docx2txt

MY_TEXT = docx2txt.process("se resume.docx")


with open("Resume.txt", "w") as text_file:
    print(MY_TEXT, file=text_file)
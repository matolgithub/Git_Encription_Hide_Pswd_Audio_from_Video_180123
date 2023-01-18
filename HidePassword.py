from PyPDF2 import PdfFileWriter, PdfFileReader, PdfWriter, PdfReader
from getpass import getpass


def main():
    pdfwriter = PdfWriter()
    pdf = PdfReader("pdf/file.pdf")

    for page in range(len(pdf.pages)):
        pdfwriter.add_page(pdf.pages[page])

    password = getpass(prompt="Input your password: ")
    pdfwriter.encrypt(password)

    with open("pdf/protect/protected_file.pdf", "wb") as protected_file:
        pdfwriter.write(protected_file)


if __name__ == "__main__":
    main()

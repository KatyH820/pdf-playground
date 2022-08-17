import PyPDF2

with open('dummy.pdf', 'rb') as file:  # use rb (read binary) when working with pdf, it convert the file object to binary mode so that the PYPDF2.PdfFileReader can read the binary object
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)  # number page
    page = reader.getPage(0)  # page object
    page.rotateCounterClockwise(90)
    # update our dummy.pdf to actually write and rotate counterclockwise.
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file:
        writer.write(new_file)

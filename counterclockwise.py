import PyPDF2
import sys
import os.path
# python3 counterclockwise.py file_to_rotate degree


def CounterClockwise(filename, degree):
    assert type(degree) is int, 'Please enter int for degree'
    assert os.path.exists(filename) == True, "File doesn't exist"
    assert os.path.isfile(filename) == True, "Input is not a file"
    with open(filename, 'rb') as file:  # use rb (read binary) when working with pdf, it convert the file object to binary mode so that the PYPDF2.PdfFileReader can read the binary object
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)  # page object
        page.rotateCounterClockwise(degree)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('tilt.pdf', 'wb') as new_file:
            writer.write(new_file)


if __name__ == '__main__':
    filename, degree = sys.argv[1:]
    degree = int(degree)
    CounterClockwise(filename, degree)

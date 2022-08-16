import PyPDF2
import sys

# python3 watermark.py (name of the file that want to add watermark) (watermark file)

def add_watermark(file, mark):
    with open(file, 'rb') as f, open(mark, 'rb') as w:
        result = PyPDF2.PdfFileWriter()
        file = PyPDF2.PdfFileReader(f)
        watermark = PyPDF2.PdfFileReader(w)
        mark = watermark.getPage(0)
        for i in range(file.numPages):
            page = file.getPage(i)
            page.mergePage(mark)
            result.addPage(page)
            with open("watermarked_output.pdf", 'wb') as r:
                result.write(r)


if __name__ == '__main__':
    file, mark = sys.argv[1:]
    add_watermark(file, mark)

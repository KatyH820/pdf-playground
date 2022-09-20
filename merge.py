import sys
import PyPDF2

# python3 merge.py file1 file2


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('combined.pdf')


if __name__ == '__main__':
    inputs = sys.argv[1:]
    pdf_combiner(inputs)

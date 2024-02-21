import pyPDF2

pdfiles = ["1.pdf","2.pdf","sample.pdf"]
merger = pyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename,  'rb')
    pdfReader = pyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')
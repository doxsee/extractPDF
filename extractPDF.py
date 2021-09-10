import re
import PyPDF2
import csv
import os

directory = '.'

for filename in os.listdir(directory):
    x = os.path.join(directory, filename)
    f = open('PO-GoodsMarking.csv', 'a', newline='')
    writer = csv.writer(f)

    if ".pdf" in x:
        pdfFileObj = open(x, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)

        s = pageObj.extractText()

        pdfFileObj.close()

        purchaseOrder = re.findall(r'\d{10}Our purchase order', s)

        goodsMarking = re.findall(r'\d{10}\s\S\S\s.\d.\d', s)

        row = purchaseOrder + goodsMarking

        writer.writerow(row)

    f.close()

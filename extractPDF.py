import re
import PyPDF2
import csv
import os


directory = '..\extractPDF'

for filename in os.listdir(directory):
    x = os.path.join(directory, filename)
    f = open('PO-GoodsMarking.csv', 'a', newline='')
    writer = csv.writer(f)
    if ".pdf" in x:
        print(x)
        pdfFileObj = open(x, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        pageObj = pdfReader.getPage(0)

        s = pageObj.extractText()

        pdfFileObj.close()

        purchaseOrder = re.findall(r'.{10}Our purchase order', s)
        purchaseOrder = re.findall(r'\d{10}', str(purchaseOrder))

        goodsMarking = re.findall(r'Goods Marking.{50}', s)
        goodsMarking = re.findall(r'\d{3}.\d{3}.{22}', str(goodsMarking))
        goodsMarking = re.findall(r'.{10}\s\S\S\s.{3}', str(goodsMarking))

        row = purchaseOrder + goodsMarking

        writer.writerow(row)

    f.close()

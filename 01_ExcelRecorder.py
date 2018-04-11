# Excel by Uncle Engineer
# www.facebook.com/UncleEngineer
# pip install openpyxl
from openpyxl import Workbook

excelfile = Workbook()
row = excelfile.active
row.append(['Product','Amount','Price'])


product = ''

while product!='s':
    product = input("Enter Product Name: ")
    
    if product!= 's':
        amount = int(input("Enter Amount: "))
        price = int(input("Price: "))
        row.append([product,amount,price])
    else:
        break

filename = input("Enter file name: ")
filename = filename + ".xlsx"
excelfile.save(filename)
print("Excel Saved: ",filename)

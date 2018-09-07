

import xlrd

# Give the location of the file
loc = ("C:\Python27\PyProject\IndianBank.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
sheet.cell_value(0, 0)

a = []

for i in range(sheet.nrows):



    if sheet.cell_value(i,0) == "Value Date":

        for y in range(i,sheet.nrows):
            if sheet.cell_value(y, 0) == "Total":
                break

            a.append(sheet.row_values(y))
        for i in a:
            print i





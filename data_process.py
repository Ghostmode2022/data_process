import xlrd
import numpy as np
import xlwt
from xlwt import Workbook
from xlutils.copy import copy
workbook = xlrd.open_workbook('/home/siddharth/Desktop/data_mining_task_1_training_data.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
sheet2 = workbook.sheet_by_name('Sheet2')
num_rows = worksheet.nrows
num_cols = worksheet.ncols
print(num_cols)
print(num_rows)

data0= [0]*num_rows
data1= [0]*num_rows
data2= [0]*num_rows

for i in range(0, num_rows):
  data0[i] = int(worksheet.cell_value(i,0))
  data1[i] = int(worksheet.cell_value(i,1))
  data2[i] = int(worksheet.cell_value(i,2))

zipped_list = zip(data0, data1, data2)

print(zipped_list)

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

for i in range(1, max(data0))
  for j in range(1, max(data1))
    sheet.write(workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

for index, value in enumerate(data):
    sheet.write(0, index, value)

workbook.save('output.xls'))


#for row_indx in enumerate(data0):
#  for col_indx in enumerate(data1):
#    sheet.write(row_indx, col_indx, 'value')

#workbook.save('output.xls')

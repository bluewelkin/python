#-*- coding:utf-8 –*-
import xlrd
#导入包的位置
#C:\Python27\Lib\site-packages
data = xlrd.open_workbook('dgx2.xls')
table = data.sheets()[0] 
total = table.nrows
print '总共有 %d 支股票' %total
'''
多行注释
cell_A1 = table.cell(1,2).value  
print cell_A1
'''
zhanting =0

for i in range(total ):
    #      print table.row_values(i)
      value = table.col(2)[i].value
      rowvalue=table.col(0)[i].value
      if(value>9.9):
          zhanting=zhanting+1
       
      if value>9.7 and value<9.9 :
          print '尾盘没有封死的股票有 %s' %rowvalue
          
print '沪深股票总共有%d支股票涨停' %zhanting

import pandas as pd
import openpyxl

df = pd.read_excel('20230720.xlsx')
data=df.values
DTList=data.tolist()
wb = openpyxl.Workbook()
ws = wb.active
for lines in DTList:
   strlines=str(lines)
   tem_line=strlines.split(',')
   tem=tem_line[1].split(' ')
   tem_line[1]=tem[1]
   tem=tem_line[0]
   tem_line[0]=tem[2]
   tem=tem_line[-1]
   tem_line[-1]=tem[0]
   del tem_line[3:(len(tem_line)+1):2]
   del tem_line[0]
   ws.append(tem_line)
wb.save(filename='CHY20230724Ver.xlsx')




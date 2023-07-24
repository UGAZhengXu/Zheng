import pandas as pd
import numpy as np
import openpyxl 

df = pd.read_excel('20230720.xlsx')
data=df.values
DTList=data.tolist()
strlines0=str(DTList[0])
tem_line0=strlines0.split(',')
print(tem_line0[1])
wb = openpyxl.Workbook()
ws = wb.active
i=0
Newfile=open('CHY.csv','w')
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
   row=np.array(tem_line)
   ws.append(tem_line)
   if i==0:
      print(tem_line)
      print(type(tem_line))
      print(len(tem_line))
      arr=np.empty((0,len(tem_line)))
      arr=np.append(arr,[row],axis=0)
   i=i+1
print(arr)
print(type(arr))
wb.save(filename='CHY20230724.xlsx')
#   print(tem_line)




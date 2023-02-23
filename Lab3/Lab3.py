# Part 1: Task 1
# Response: Finshed by created messy.ssv

# Part 1: Task 2
Data=open('messy.ssv','r')
Datalines=Data.readlines()

# Part 1: Task 3
def funPart1(Var1):
    Sp_Var1=Var1.split(";")
    Name_Ori=Sp_Var1[0]
    Gender_Ori=Sp_Var1[1]
    Email_Ori=Sp_Var1[2]
    Age_Ori=Sp_Var1[3]
    Hight_Ori=int(Sp_Var1[4])
    Weight_Ori=int(Sp_Var1[5])
    tem = 0
    try:
      Name_Sp=Name_Ori.split(",")
      Name_First=Name_Sp[1]
      Name_Last=Name_Sp[0]
    except:
          try:
           Name_Sp=Name_Ori.split(" ")
           Name_First=Name_Sp[0]
           Name_Last=Name_Sp[1]
          except:
           Name_First=Name_Ori
           Name_Last='Unknown'
           tem = 1
          pass
    pass
    try:
      AgeNew=int(Age_Ori)
    except:
      AgeNew=-1
      tem = 1
    pass

    if  Hight_Ori>100:
        HightNew = Hight_Ori
        WeightNew = Weight_Ori
    else:
        HightNew = Hight_Ori*2.54
        WeightNew= Weight_Ori*0.45359237
        tem = 1
    ListRe=[Name_First,Name_Last,Gender_Ori[0],AgeNew,HightNew,WeightNew,Email_Ori,tem]
    return ListRe

# Part 1: Task 4
FirstName=[]
LastName=[]
Gender=[]
Age=[]
Hight=[]
Weight=[]
Email=[]
Issue=[]

# Code 1 (using reverse())
ReverseData=Datalines[::-1]
for lines in ReverseData:
     tem_line=funPart1(lines)
     if tem_line[6] in Email:
        pass
     else:
        FirstName.append(tem_line[0])
        LastName.append(tem_line[1])
        Gender.append(tem_line[2])
        Age.append(tem_line[3])
        Hight.append(tem_line[4])
        Weight.append(tem_line[5])
        Email.append(tem_line[6])
        Issue.append(tem_line[7])
FirstName.reverse()
LastName.reverse()
Gender.reverse()
Age.reverse()
Hight.reverse()
Weight.reverse()
Email.reverse()
Issue.reverse()
if len(Datalines)-len(FirstName)>1:
  print(f'There are {len(Datalines)-len(FirstName)} people reentry their information')
else:
  print(f'There is 1 person reentry their information')

# Code 2 (using index())
FirstName1=[]
LastName1=[]
Gender1=[]
Age1=[]
Hight1=[]
Weight1=[]
Email1=[]
Issue1=[]

for locationOri,lines in enumerate(Datalines):
     tem_line=funPart1(lines)    
     if tem_line[6] in Email1:
        location=Email1.index(tem_line[6])
        FirstName1[location]=tem_line[0]
        LastName1[location]=tem_line[1]
        Gender1[location]=tem_line[2]
        Age1[location]=tem_line[3]
        Hight1[location]=tem_line[4]
        Weight1[location]=tem_line[5]
        Email1[location]=tem_line[6]
        Issue1[location]=tem_line[7]
     else:
        FirstName1.append(tem_line[0])
        LastName1.append(tem_line[1])
        Gender1.append(tem_line[2])
        Age1.append(tem_line[3])
        Hight1.append(tem_line[4])
        Weight1.append(tem_line[5])
        Email1.append(tem_line[6])
        Issue1.append(tem_line[7])

if len(Datalines)-len(FirstName1)>1:
  print(f'There are {len(Datalines)-len(FirstName1)} people reentry their information')
else:
  print(f'There is 1 person reentry their information')
# There have some difference among the sequence of these two methods
print(FirstName,FirstName1)

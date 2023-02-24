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
        HightNew = int(Hight_Ori*2.54)
        WeightNew= int(Weight_Ori*0.45359237)
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
# However, all the elements containing is the same
print(FirstName,FirstName1)

# Part 2: Task 1
# using traditional method; can also use numpy
Age_tem=[]
for i,n in enumerate(Age1):
    sum=0
    k=0
    if n<0:
        pass
    else:
        Age_tem.append(Age1[i])
        sum=sum+Age1[i]
        k=k+1
Age_Ave=sum/k
lenAgetem=len(Age_tem)
Agesorted=sorted(Age_tem)
if lenAgetem%2==0:
   Age_mid=round((Agesorted[lenAgetem/2]+Agesorted[lenAgetem/2-1])/2)
else:
   Age_mid=Agesorted[int((lenAgetem-1)/2)]
NewAge=Age1[:]
for i,n in enumerate(NewAge):
    if n<0:
        NewAge[i] = Age_mid
print('The Orginal Age is:',Age1)
print('The Orginal Modified Age is:',NewAge)
print(f'The age range is [{Agesorted[0]},{Agesorted[-1]}]')

# Part 2: Task 2
Hight_Unit=[x/100 for x in Hight1]
BMI=[]
for i,w in enumerate(Weight1):
   BMI.append(w/(Hight_Unit[i]**2))
print('BMI(kg/m^2):',BMI)

# Part 2: Task 3
Newfile=open('clean.ssv','w')
for i,n in enumerate(Age1):
   temstri=[FirstName1[i],LastName1[i],Gender1[i],Email1[i],str(NewAge[i]),str(Hight1[i]),str(Weight1[i]),str(Issue1[i])]
   Newfile.writelines([';'.join(temstri),'\n'])

# Part 3: Task 1



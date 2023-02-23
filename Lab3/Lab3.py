# Part 1: Task 1
# Response: Finshed by created messy.ssv

# Part 1: Task 2
Data=open('messy.ssv','r')
Datalines=Data.readlines()
print(Datalines)

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
           Name_First=Name_Ori[0]
           Name_Last='Unknown'
           tem = 1
          pass
    pass
    try:
      Age=int(Age_Ori)
    except:
      Age=-1
      tem = 1
    pass

    if  Hight_Ori>100:
        Hight = Hight_Ori
    else:
        Hight = Hight_Ori*2.54
        Weight= Weight_Ori*0.45359237
        tem = 1
    ListRe=[Name_First,Name_Last,Gender_Ori[0],Age,Hight,Weight,Email_Ori,tem]
    return ListRe

print(funPart1(Datalines[0]))
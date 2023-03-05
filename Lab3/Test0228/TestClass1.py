from dataclasses import dataclass

# @dataclass
# class MydataClass:
#     A:int=3

class MyClass1:
    # A = 3
    def __init__(self,num):
        self.A=num              
        # print(self)
        pass
    def doubleIt(self):
        self.A *=2
    def __str__(self):
        return f"The value is: {self.A}"

if __name__=="__main__":
    obj = MyClass1(4)
    MyClass1.doubleIt(obj)
    obj.doubleIt()

    # Obj2=MydataClass()
    # obj.__init__()

    # MyClass1.__init__(3)
    
    # # obj.A=3
    # print(dir(obj))
    # print(obj.__dict__)
    print(obj.A)
    print(obj)
    print(str(obj))
    # print(type(obj))
    pass

a_list = [1,2,3]
a_new_list=[x+1 for x in a_list if x>1]
print(a_new_list)
quick_list=[x*x for x in range(7)]
print(quick_list)

def normal_function(var1):
    return var1
a_Fun=normal_function
a_Fun(3)
print(a_Fun(4))

a_fun= lambda x:x*x
print(list(map(a_fun,[1,2,3])))

def b_fun(var1):
    return var1*var1
print(list(map(b_fun,[1,2,3])))

print(list(map(lambda x:x*x,[1,2,3])))

a_string = '123'
int(a_string)

b_string ='123a'
try:
    int(b_string)
except:
    print('Invaild')
    pass
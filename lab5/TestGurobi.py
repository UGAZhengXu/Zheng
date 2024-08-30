import gurobipy as gp
import numpy as np
import math as MT
import torch as TCH

# https://github.com/hwiberg/OptiCL （ML+MIP）

m=gp.Model("TestLP")
a=np.ones([1,5])
# b=np.array([[1,1,2],[1,2,4]])
b=np.ones([2,5])
c=np.ones([1,2])*10
d=np.ones([2,1])*10
print(c)

# Creat Variables
# x=m.addVar(vtype=gp.GRB.CONTINUOUS,lb=3, ub=6,name="x")
x=m.addVar(vtype=gp.GRB.CONTINUOUS,lb=-MT.inf,ub=MT.inf,name="x")
y=m.addVar(vtype=gp.GRB.CONTINUOUS,lb=-MT.inf,ub=MT.inf,name="y")

z=m.addMVar(5,1,vtype=gp.GRB.CONTINUOUS,name="z")

# Set Objective
obj=x+y+a@z
m.setObjective(obj)

# Add Constraints
m.addConstr(2*x+3*y<=15,"a0")
m.addConstr(y>=-3,"a1")
# m.addConstr(y==gp.abs_(x))
m.addConstr(x>=y,"a2")
m.addConstr(z>=2,name="c3")
m.addConstr(b@z>=c,name="c4") 
m.addConstr(b@z>=d,name="c5") 


# Write model to file
m.write("TestLP.lp")
m.optimize()
for i in m.getVars():
    print('%s=%g ' % (i.varName,i.x), end = "")
dual0=m.getAttr("Pi",m.getConstrs())
print("dual_all=", dual0)
c4name=m.getConstrByName("c4[0,1]")
print(c4name.constrName, '=', c4name.Pi)
C4all=[m.getConstrByName("c4[0,{}]".format(i)).Pi for i in range(len(b))]
print(C4all)
C4constr=[m.getConstrByName("c4[0,{}]".format(i)) for i in range(len(b))]
dualc4=m.getAttr("Pi",C4constr)
print("dual4=", dualc4)
C5allBi=[m.getConstrByName("c5[{},{}]".format(i,j)).Pi for i in range(len(b)) for j in range(len(b))]
print("dual5bi=", C5allBi)

for i in range(len(b)):
    for j in range(len(b)):
        C5ij=[m.getConstrByName("c5[{},{}]".format(i,j)).Pi]
        print("c5[{},{}]:".format(i,j),C5ij)
print(type(C5allBi))
#print("dual_c4=", c4name)
m.write('m.lp')
import pyomo.environ as pyo

m = pyo.ConcreteModel()


m.r11=pyo.Var(within = pyo.NonNegativeIntegers)
m.r12=pyo.Var(within = pyo.NonNegativeIntegers)
m.r21=pyo.Var(within = pyo.NonNegativeIntegers)
m.r22=pyo.Var(within = pyo.NonNegativeIntegers)
m.r31=pyo.Var(within = pyo.NonNegativeIntegers)
m.r32=pyo.Var(within = pyo.NonNegativeIntegers)

m.o11=pyo.Var(within = pyo.NonNegativeIntegers)
m.o12=pyo.Var(within = pyo.NonNegativeIntegers)
m.o21=pyo.Var(within = pyo.NonNegativeIntegers)
m.o22=pyo.Var(within = pyo.NonNegativeIntegers)
m.o31=pyo.Var(within = pyo.NonNegativeIntegers)
m.o32=pyo.Var(within = pyo.NonNegativeIntegers)

m.v11=pyo.Var(within = pyo.NonNegativeIntegers)
m.v12=pyo.Var(within = pyo.NonNegativeIntegers)
m.v21=pyo.Var(within = pyo.NonNegativeIntegers)
m.v22=pyo.Var(within = pyo.NonNegativeIntegers)


def obj_rule(m):
    return (15*m.r11+16*m.r12+17*m.r21+15*m.r22+19*m.r31+17*m.r32+
            18*m.o11+20*m.o12+20*m.o21+18*m.o22+22*m.o31+22*m.o32+
            1*m.v11+2*m.v12+2*m.v21+1*m.v22)
m.obj=pyo.Objective(rule=obj_rule,sense=pyo.minimize)

def sale_const1(m,i):
    return m.r11+m.r12 <=10
m.sale_const1=pyo.Constraint(rule=sale_const1)

def sale_const2(m,i):
    return m.r21+m.r22 <=8
m.sale_const2=pyo.Constraint(rule=sale_const2)

def sale_const3(m,i):
    return m.r31+m.r32 <=10
m.sale_const3=pyo.Constraint(rule=sale_const3)

def sale_const4(m,i):
    return m.o11+m.o12 <=3
m.sale_const4=pyo.Constraint(rule=sale_const4)

def sale_const5(m,i):
    return m.o21+m.o22 <=2
m.sale_const5=pyo.Constraint(rule=sale_const5)

def sale_const6(m,i):
    return m.o31+m.o32 <=3
m.sale_const6=pyo.Constraint(rule=sale_const6)

def storage_const1(m,i):
    return m.r11+m.o11-m.v11 >=5
m.storage_const1=pyo.Constraint(rule=storage_const1)

def storage_const2(m,i):
    return m.r12+m.o12-m.v12 >=3
m.storage_const2=pyo.Constraint(rule=storage_const2)

def storage_const3(m,i):
    return m.r21+m.o21-m.v21+m.v11 >=3
m.storage_const3=pyo.Constraint(rule=storage_const3)

def storage_const4(m,i):
    return m.r22+m.o22-m.v22+m.v12 >=5
m.storage_const4=pyo.Constraint(rule=storage_const4)

def storage_const5(m,i):
    return m.r31+m.o31+m.v21 >=4
m.storage_const5=pyo.Constraint(rule=storage_const5)

def storage_const6(m,i):
    return m.r32+m.o32+m.v22 >=4
m.storage_const6=pyo.Constraint(rule=storage_const6)



pyo.SolverFactory('glpk').solve(m)
m.pprint()
m.display() #shows the constraints

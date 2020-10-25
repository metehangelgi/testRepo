import pyomo.environ as py

m = py.ConcreteModel()

m.x11 = py.Var(within = py.NonNegativeIntegers)
m.x12 = py.Var(within = py.NonNegativeIntegers)
m.x13 = py.Var(within = py.NonNegativeIntegers)

m.x21 = py.Var(within = py.NonNegativeIntegers)
m.x22 = py.Var(within = py.NonNegativeIntegers)
m.x23 = py.Var(within = py.NonNegativeIntegers)

m.x31 = py.Var(within = py.NonNegativeIntegers)
m.x32 = py.Var(within = py.NonNegativeIntegers)
m.x33 = py.Var(within = py.NonNegativeIntegers)

m.x41 = py.Var(within = py.NonNegativeIntegers)
m.x42 = py.Var(within = py.NonNegativeIntegers)
m.x43 = py.Var(within = py.NonNegativeIntegers)

m.x51 = py.Var(within = py.NonNegativeIntegers)
m.x52 = py.Var(within = py.NonNegativeIntegers)
m.x53 = py.Var(within = py.NonNegativeIntegers)


M = 100000000

def obj_rule(m):
    return (31*m.x11 + 45*m.x12 + 38*m.x13 + 
            29*m.x21 + 41*m.x22 + 35*m.x23 + 
            32*m.x31 + 46*m.x32 + 40*m.x33 + 
            28*m.x41 + 42*m.x42 + M*m.x43 + 
            29*m.x51 + 43*m.x52 + M*m.x53)
m.objective = py.Objective(rule = obj_rule, sense = py.minimize)

def cons1(m):
    return 31*m.x11 + 29*m.x21 + 32*m.x31 + 28*m.x41 + 29*m.x51 >= 600
m.cons1 = py.Constraint(rule = cons1)

def cons2(m):
    return 45*m.x12 + 41*m.x22 + 46*m.x32 + 42*m.x42 + 43*m.x52 >= 1000
m.cons2 = py.Constraint(rule = cons2)

def cons3(m):
    return 38*m.x13 + 35*m.x23 + 40*m.x33 + M*m.x43 + M*m.x53 >= 800
m.cons3 = py.Constraint(rule = cons3)

def cons4(m):
    return 31*m.x11 + 45*m.x12 + 38*m.x13 <= 400
m.cons4 = py.Constraint(rule = cons4)

def cons5(m):
    return 29*m.x21 + 41*m.x22 + 35*m.x23 <= 600
m.cons5 = py.Constraint(rule = cons5)

def cons6(m):
    return 32*m.x31 + 46*m.x32 + 40*m.x33 <= 400
m.cons6 = py.Constraint(rule = cons6)

def cons7(m):
    return 28*m.x41 + 42*m.x42 + M*m.x43 <= 600
m.cons7 = py.Constraint(rule = cons7)

def cons8(m):
    return  29*m.x51 + 43*m.x52 + M*m.x53 <= 1000
m.cons8 = py.Constraint(rule = cons8)


py.SolverFactory("glpk").solve(m)
m.pprint()
m.display() #shows the constraints
m.display() #shows the constraints


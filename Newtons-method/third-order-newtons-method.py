# Third order Newton's method

max_steps = 50 ## max number of iterations to use
x0 = 2.

def f(x):
    return x**3 - 2.

def fp(x):
    return 3*x**2

def fpp(x):
    return 6*x

def third_order():
    global x
    x = []
    x.append(x0)
    for i in range(max_steps):
        x.append(x[i] - f(x[i])/fp(x[i]) - (fpp(x[i])*f(x[i])**2)/(fp(x[i])**3))
    return x

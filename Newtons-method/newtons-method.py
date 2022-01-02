import numpy
import matplotlib

Nsteps = 8
x0 = 1.2
xhat = 0.

def f(x):
    return x^2

def fprime(x):
    return 2*x

def newton():
    # newtons method
    global xhat
    for i in range(Nsteps):
        xhat = xhat - f(xhat)/fprime(xhat)
    return xhat
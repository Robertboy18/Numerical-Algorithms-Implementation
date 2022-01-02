# Finding roots of the polynomial using bisection and newtons's method
import numpy 
import matplotlib

Nsteps = 50 ## we will run a fixed number of steps instead of testing for an error tolerance (step 2)
a = -10
b = 10

def f(x):
    return x**3 -9*x**2 +11*x-11

def bisection(a,b,Nsteps):
    x = zeros(Nsteps)
    for j in arange(Nsteps):
        c = (a + b)/2.
        x[j] = c
        if f(c)*f(b) < 0:
            a = c
        else:
            b = c
        if f(c) == 0.: ## this is for the unlikely event that we find the exact root
            break
    return c

def fprime(x):
    return 3*x**2 -18*x +11

def newton(Nsteps,x0 = bisection(a,b,Nsteps)):
    x = zeros(Nsteps)
    x[0] = x0
    for j in arange(Nsteps-1):
        x[j+1] = x[j] - f(x[j])/fprime(x[j])
        if abs(x[j+1] - x[j]) < 1e-6:
            print("Root of the polynomial :",x[j+1])
            break

newton(Nsteps)

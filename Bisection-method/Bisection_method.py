import numpy

"""
In mathematics, the bisection method is a root-finding method that applies to any continuous 
functions for which one knows two values with opposite signs. 
The method consists of repeatedly bisecting the interval defined by these values '
and then selecting the subinterval in which the function changes sign, and therefore must contain a root.
It is a very simple and robust method, but it is also relatively slow
Given a continuous function f(x) and an open interval (a, b) such that a<b and f(a)f(b) < 0,
  1. Set c = (a+b)/2
  2. If |c-a| < tol end and return c
  3. If f(c)f(b) < 0 then set a = c, otherwise set b = c
  4. repeat step 1

"""

Nsteps = 50 ## we will run a fixed number of steps instead of testing for an error tolerance (step 2)
a = -10
b = 10

def f(x):
    # example function
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

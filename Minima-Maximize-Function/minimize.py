import math
import numpy as np
import scipy
from scipy import optimize

def f(Z):
    X,Y = Z
    return 2*X**3 - 3*X**2 - 6*X*Y*(X - Y - 1)

print("Minimize f")

print("-"*100)

x = uniform(-2,2,2)
y = uniform(-2,2,2)
for i in x:
    for j in y:
        x0 = [i,j]
        result = scipy.optimize.fmin(f, x0, maxiter = 20, retall = True)
        print("Initial Guess",x0,"Result ",result,sep = "\n")
        print("*"*100)

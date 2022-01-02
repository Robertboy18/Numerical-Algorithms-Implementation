import math
import numpy as np
import scipy
from scipy import optimize


def g(Z):
    X,Y = Z
    return -2*X**3 + 3*X**2  + 6*X*Y*(X - Y - 1)

print("Minimize - f = Maximize f")

print("-"*100)

# toggle to check the result from the scipy library
for i in x:
    for j in y:
        x0 = [i,j]
        result = scipy.optimize.fmin(g, x0, maxiter = 20, retall = True)
        print("Initial Guess",x0,"Result ",result,sep = "\n")
        print("*"*100)
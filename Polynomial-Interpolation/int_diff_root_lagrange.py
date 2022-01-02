import numpy
from Lagrange_Polynomials import evaluation
from chebyshev_nodes import chebyshev_nodes, chebyshev_fit
from Derivative_Lagrange import differentiate_lagrange
from Integration_Lagrange  import Integration_Lagrange
from root_finding import root_finding

n = 100
a = 0.
b = 10.

def f(x):
    y = [0]*len(x)
    y = [exp(i)**3/2 for i in x]
    return array(y)

xnodes = chebyshev_nodes(a, b, n)
weights = chebyshev_fit(n)
ynodes = f(xnodes)

# derivative
x = linspace(a, b, 301) 
yexact = f(x)

# derivative and integration
p = evaluation(x, xnodes, ynodes, weights)
p_prime = differentiate_lagrange(x, xnodes, ynodes, weights)
P = Integration_Lagrange(x, xnodes, ynodes, weights)

# root finding
p = evaluation(x, xnodes, ynodes, weights)
xroots = root_finding(xnodes, ynodes, weights)
import numpy

n = 100
a = 0.
b = 10.

xnodes = chebyshev_nodes(a, b, n)
weights = baryfit_chebyshev(n)
ynodes = ftest(xnodes)

x = linspace(a, b, 301) 
yexact = ftest(x)
dydxexact = fptest(x)


p = baryeval(x, xnodes, ynodes, weights)
p_prime = barydiff(x, xnodes, ynodes, weights)
P = baryint(x, xnodes, ynodes, weights)
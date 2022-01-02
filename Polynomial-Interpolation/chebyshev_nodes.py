import numpy as np

# Lebesgue constant 
# L_j(x) = Pi_{i=0}^{j} (x - x_i)/(x_j - x_i)
# delta_n = max{a<=x<=b} sum_{i=0}^{n} |L_i(x)|

"""
Let $x_0, x_1, \ldots x_n$  be distinct nodes, and suppose $p(x)$ and $\hat{p}(x)$ are polynomials of degree at most $n$ satisfying $p(x_j) = y_j$ and $\hat{p}(x_j) = \hat{y}_j$, $j=0,1,\ldots, n$. If
$$  \vert y_j - \hat{y}_j\vert \leq \delta,  \quad j=0,1,\ldots, n,$$
then
$$ \Vert p - \hat{p} \Vert_{\infty} \leq \Lambda_n \delta.$$
"""

# cheyshev nodes are given by 
def chebyshev_nodes(n):
    # the lebesgue constant for chebyshev nodes is 
    # Delta_n = O(log(n))
    j = arange(n+1)
    return (a + b)/2 - (b - a)/2*cos(j*pi/n)

def chebyshev_fit(n):
    j = arange(n+1)
    d = ones(n+1)
    d[0] = 0.5
    d[-1] = 0.5
    return (-1)**j*d


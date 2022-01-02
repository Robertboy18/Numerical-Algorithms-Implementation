import numpy

def cyclic_swap(x, i, j, k, xhat):
    x[i], x[j], x[k] = x[j], x[k], xhat

def f(x):
    return x**4 - 2*x**3 + 3*x**2 - 2*x + 1

## it is a minimization method that does not use the gradient
def parabolic_search(f, a, b, tol, maxiter=100):
    """
    Successive parabolic interpolation is a technique
    for finding the extremum (minimum or maximum) of a
    continuous unimodal function by successively fitting parabolas 
    (polynomials of degree two) to a function of one variable at three unique points or,
    in general, a function of n variables at 1+n(n+3)/2 points, 
    and at each iteration replacing the "oldest" point with the extremum of the fitted parabola.
    # https://web.engr.oregonstate.edu/~webbky/MAE4020_5020_files/Section%205%20Root%20Finding%20and%20Optimization.pdf
    # MATH 381
    """
    c = (a + b)/2
    inds = array([f(a), f(b), f(c)]).argsort()
    x = array([a, b, c])[inds]
    y = array([f(xi) for xi in x])
    n = 0
    while absolute(x[-1] - x[1]) > tol and n < maxiter:
        p = (x[2] - x[0])**2*(y[2] - y[1]) - (x[2] - x[1])**2*(y[2] - y[0])
        q = ((x[2] - x[0])*(y[2] - y[1]) - (x[2] - x[1])*(y[2] - y[0]))
        xhat = x[2] - 0.5*(p/q)
        cyclic_swap(x, 0, 1, 2, xhat)
        cyclic_swap(y, 0, 1, 2, f(xhat))
        n += 1
    if n >= maxiter:
        print("max iterations reached without convergence")
    return x[-1]

# example
tol = 10.**-4
xmin = parabolic_search(f, -pi, 2*pi, tol, 1000)
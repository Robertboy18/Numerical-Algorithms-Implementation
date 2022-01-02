import numpy 
from Lagrange_Polynomials import evaluation
from chebyshev_nodes import chebyshev_nodes, chebyshev_fit

# function to compute the derivative of a lagrange polynomial 
def Integration_Lagrange(x, xnodes_old, ynodes_old, weights_old ):
    """
    Indefinite integral of a lagrange polynomial in barycentric
    integral_{a}^{x} p(u) du   
    """
    n = len(xnodes_old)
    xnodes = chebyshev_nodes(xnodes_old[0], xnodes_old[n-1], n)
    ynodes = evaluation(xnodes, xnodes_old, ynodes_old, weights_old)
    weights = chebyshev_fit(n)
    D = [[0]*n]*n
    for i in range(n+1):
        for j in range(n+1):
            if i != j:
                D[i][j] = weights[j]/(weights[i]*(xnodes[i] - xnodes[j]))
    diagonal = -array(D).sum(axis=1)
    for i in range(len(xnodes)+1):
        D[i, i] = diagonal[i]
    D[0, :], D[0, 0] = 0, 1 ## set first element of first row to one
    matrix = [0]*(n+1)
    matrix[1:] = ynodes[1:]
    final_nodes = numpy.linalg.solve(D, matrix)
    integral_px = evaluation(x, xnodes, final_nodes, weights)
    return integral_px
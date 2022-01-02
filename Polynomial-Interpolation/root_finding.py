import numpy
import scipy.linalg

# find the roots of the lagrange polynomial
def roots(xnodes, ynodes, weights):
    n = len(xnodes)
    D = [[0]*(n+2)]*(n+2)
    D[1:][0], D[0][1:] = weights, -ynodes
    for i in range(1, n+2):
        D[i][i] = xnodes[i-1]
    B = numpy.eye(n+2) ## builds the identity matrix
    B[0, 0] = 0
    # find the generalized eigenvalues of D
    L, _ = scipy.linalg.eig(D,B) 
    return L[numpy.isfinite(L)]
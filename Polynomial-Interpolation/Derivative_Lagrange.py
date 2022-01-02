import numpy 
from Lagrange_Polynomials import evaluation

# function to compute the derivative of a lagrange polynomial 
def differentiate_lagrange(x, xnodes, ynodes, weights):
    """
    https://math.stackexchange.com/questions/809927/first-derivative-of-lagrange-polynomial
    L'_i(x) = L_j(x) \sum_{j=0}^{n}{j =\= i} 1/(x - x_j)
    """
    D = [[0]*len(xnodes)]*len(xnodes)
    for i in range(len(xnodes)+1):
        for j in range(len(xnodes)+1):
            if i != j:
                D[i][j] = weights[j]/(weights[i]*(xnodes[i] - xnodes[j]))
    diagonal = -array(D).sum(axis=1)
    for i in range(len(xnodes)+1):
        D[i, i] = diagonal[i]
    derivative = matrix(D)*matrix(ynodes[:, None])
    yprimenodes = array(derivative).squeeze()
    return evaluation(x, xnodes, yprimenodes, weights)
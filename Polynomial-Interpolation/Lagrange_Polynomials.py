import numpy
from functions import f

# interpolation error by barycentric is 
# |f - p| <= (||f^(n+1)||_inf/(n+1)!) pi_{i=0}^{n} | x - x_i |

def centrix_weights(xnodes):
    """
    computing the barycentric weights
    w_j = 1/(pi*(x_j - x_i) { j \= i})
    Inputs : nodes x_j 
    output : weights w_j
    
    """
    weights = [0]*len(xnodes)
    for j in range(len(xnodes)):
        w = 1
        for i in range(len(xnodes)):
            if i != j:
                w = w * (1/(xnodes[j] - xnodes[i]))
        weights[j] = w
    return weights

def evaluation(xnodes,weights,fvalues,value):
    """
    Evaluating the barycentric interpolant p(x)
    p(x) = \sum_{j=0}^{n} ((w_j f(x_j))/(x-x_j))/ (\sum_{j=0}^{n} w_j/(x-x_j))
    where w_j = 1/(pi*(x_j - x_i) { j \= i})
    Inputs: nodes x_j, weights w_j, f(x_j) and the location of where teh interpolant should be evaluated
    Output: p(x) at all the evaluation points
    """
    num = 1
    sum1 = 0
    sum2 = 0
    for j in range(len(xnodes)):
        if value != xnodes[j]:
            num = (weights[j]*fvalues[j])/(value - xnodes[j])
            sum1 += num
    for j in range(len(xnodes)):
        if value != xnodes[j]:
            num = (weights[j])/(value - xnodes[j])
            sum2 += num
    return sum1/sum2

# vectorized versions
def vectorized_centric_weight(xnodes):
    return 1/(xnodes[None, :] - xnodes[:, None] + eye(xnodes.size)).prod(axis=0)

# the idenity matrix eye is included so that i =\= j
def vectorized_evaluation(x, xnodes, ynodes, weights):
    bary = weights[:, None]/(x[None, :] - xnodes[:, None] + eye(xnodes.size))
    y = (bary*ynodes[:, None]).sum(axis=0)/bary.sum(axis=0)
    return y

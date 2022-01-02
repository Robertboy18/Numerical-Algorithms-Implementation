import numpy 

def backward_substitution(U, b):
    """Upper triangular matrix `U` and right hand side vector `b`. 
    """
    n = b.size
    x = ones_like(b)
    for k in range(n)[::-1]:
        q = 0.
        for j in range(k+1, n):
            q = q + U[k, j]*x[j]
        x[k] = (b[k] - q)/U[k, k]
    return x
    
def forward_substitution(L, b):
    """Lower triangular matrix `L` and right hand side vector `b`. 
    """
    x = ones_like(b)
    for k in range(n):
        q = 0.
        for j in range(k):
            q = q + L[k, j]*x[j]
        x[k] = (b[k] - q)/L[k, k]
    return x
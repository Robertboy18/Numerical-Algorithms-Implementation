import numpy 
from LU_Decomposition import backward_substitution, forward_substitution

t = linspace(0,1,50)
n = 12
m = 50
A = []
for i in range(m):
    z = []
    for j in range(n):
        z.append(t[i]**j)
    A.append(z)
A = array(A)
b = array([cos(4*t)]).T


# LU decomposition
print("Chlolesky")
M = A.T@A
L = cholesky(M) ## This returns a lower triangular matrix such that M = L@L.T
y = forward_substitution(L, A.T@b)
x = backward_substitution(L.T, y)
print('residual', norm(A@x - b))
print(x)

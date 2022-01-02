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


## If you want the full SVD decomposition, use `full_matrices=True`
print("SVD")
Uhat, sigma, Vhat_T = svd(A, full_matrices=False) ## sigma is the vector of diagonal entries, not the matrix
Vhat = Vhat_T.T
y = (1/sigma[:, None])*(Uhat.T@b) ## this is equivalent to solving Sigma_hat@y = Uhat.T@b
x = Vhat@y
print('residual', norm(A@x - b))
print(x)
from LU_Decomposition import *
import numpy

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

# Cholesky
print("Chlolesky")
M = A.T@A
L = cholesky(M) ## This returns a lower triangular matrix such that M = L@L.T
y = forward_substitution(L, A.T@b)
x = backward_substitution(L.T, y)
print('residual', norm(A@x - b))
print(x)

## If you want the full QR decomposition, use `mode='full'`
print("QR")
Qhat, Rhat = qr(A, mode='reduced') 
y = Qhat.T@b
x = backward_substitution(Rhat, y)
print('residual', norm(A@x - b))
print(x)

## If you want the full SVD decomposition, use `full_matrices=True`
print("SVD")
Uhat, sigma, Vhat_T = svd(A, full_matrices=False) ## sigma is the vector of diagonal entries, not the matrix
Vhat = Vhat_T.T
y = (1/sigma[:, None])*(Uhat.T@b) ## this is equivalent to solving Sigma_hat@y = Uhat.T@b
x = Vhat@y
print('residual', norm(A@x - b))
print(x)
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

## If you want the full QR decomposition, use `mode='full'`
print("QR")
Qhat, Rhat = qr(A, mode='reduced') 
y = Qhat.T@b
x = backward_substitution(Rhat, y)
print('residual', norm(A@x - b))
print(x)

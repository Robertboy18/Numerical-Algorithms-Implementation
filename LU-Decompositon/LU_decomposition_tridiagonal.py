import numpy 

def LU_decomposition(a,b,c):
    # for tridiagonal matrix 
    # a = main diagonal
    # b = below diagonal
    # c = above diagonal
    # else all 0
    # operation count 0(n)
    n = len(a)
    b.insert(0,0)
    l = [0]*n
    u = [0]*n
    u[0] = a[0]
    for i in range(1,n):
        l[i] = b[i]/u[i-1]
        u[i] = a[i] - l[i]*c[i-1]
        
    return l[1:],u

a = ([i for i in range(1,11)])
b = ([-i/2 for i in range(2,11)])
c = ([-i/2 for i in range(1,10)])
z,k = LU_decomposition(a,b,c)

print(z,k,sep = "\n")
import numpy

def algo_pseudo(m = 23,n = 1):
    # generate random dataset
    y = uniform(-5,6,23)
    m = 23
    A = []
    for i in range(m):
        z = []
        for j in range(n):
            z.append(y[i]**j)
        A.append(z)
    A = array(A)
    b = sin((pi/5)*y) + y/5
    return y,A,b

def pseudo_ls(A,b,tol):
    # main algorithm 
    # A = Matrix in R^(m,n)
    # we don't assume that its full rank or that m > n
    # we also have a tol >= 0 such that any singular value sigma_i < tol is set to zero
    # we first find the rank r of the Full SVD Decomosition of A ie U,sigma,V
    # Now U is m x r and sigma is r x r and V is r x n
    # then A_{psuedo} = V*Sigma^-1*U^T
    b = b.T
    Uhat, sigma,V_hat = svd(A)
    sigma_hat = []
    for i in range(len(sigma)):
        if sigma[i] < tol:
            sigma_hat.append(0)
        else:
            sigma_hat.append(pow(sigma[i],-1))
    sigma_hat = array(sigma_hat)
    s_inv = np.zeros(A.shape)
    s_inv[0][0] = sigma_hat[0]
    s_inv[1][1] = sigma_hat[1]
    
    pseudo_A = V_hat.T@s_inv.T@Uhat.T
    x = pseudo_A@b
    print('residual', norm(A@x - b))
    return x

def pfun(n=2, tol_exponent=-10):
    tol = 10.**(tol_exponent)
    m = 23
    y,A,b = algo_pseudo(m, n)
    x = pseudo_ls(A, b, tol)
    print("n = ",n, "tol = ",tol)
    plot(y, b, 'k')
    plot(y, A@x, 'o')
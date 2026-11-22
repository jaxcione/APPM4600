import numpy as np
import matplotlib.pyplot as plot

def matrix(m,alpha):
    n=m-1
    A=np.zeros((n,n))

    for j in range(n):
        for k in range(n):
            if j==k:
                A[j][k]=1-2*alpha
            elif abs(j-k)==1:
                A[j][k]=alpha
    return A


def QR(m,alpha,N):
    A=matrix(m,alpha)
  
    for k in range(N):
        Q,R=np.linalg.qr(A) 
        A=np.matmul(R,Q)

        
        if  np.linalg.norm(np.tril(A, k=-1))<1E-7: # the lower triangular part of the matriix
            s=np.diag(A)
            return np.sort(s),k+1
            
        
    return None, f"Did not converge in {N} iterations"


alpha_vals=[1/4,1/2,3/4]

for s in alpha_vals:
    print()
    actual=np.linalg.eigvalsh(matrix(11,s))
    print(f"QR iteration Eigenvalues,alpha={s}: ")
    print(QR(11,s,100000)[0])
    print()
    print(f"Actual Eigenvalues,alpha={s}: ")
    print(actual)
    print(f"rho(A) = {np.max(np.abs(actual)):.6f}")
    print("-"*50)




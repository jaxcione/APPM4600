import numpy as np
import matplotlib.pyplot as plt


def matrix(n):
    A=np.empty((n,n),dtype=float)
    for j in range(n):
        for k in range(n):
            if j==k:
                A[j][k]=1
            else:
                A[j][k]=-1
    return A

def Power_method(n,M):
    A=matrix(n)
    
  
    X=np.random.rand(n)
    X=X/np.linalg.norm(X)
    lam_prev=0

    for k in range(1,M):
        v=(A@X)/np.linalg.norm(A@X)
        lam=(np.matmul(v,np.matmul(A,v)))/(np.matmul(v,v))
        X=v

        if abs(lam-lam_prev)/abs(lam)<(10)**-10:
            break

        lam_prev=lam
    
    return lam,v,k,A



N=[4]

for s in N:
    
    print("-"*50)
    print(f"Size of Matrix: {s}")
    print()
    E,v,k,A=Power_method(s,1000)
    val=np.linalg.eigvalsh(A)[-1]
    print("Eigenvalue:",E)
    print()
    print("Eigenvector:",v)
    print()
    print("Iterations:",k)
    print("Relative Error:",abs(E-val)/abs(val))

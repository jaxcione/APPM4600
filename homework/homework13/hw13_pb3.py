import numpy as np
import matplotlib.pyplot as plt

def matrix(n):
    A=np.empty((n,n),dtype=float)
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i-1][j-1]=(1)/(i+j-1)

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


def Power_method_inverse(n,M):
    A=matrix(n)
    A_inv =np.linalg.inv(A)
    X =np.random.rand(n)
    X=X/np.linalg.norm(X)
    lam_prev=0

    for k in range(1,M):
        v=(A_inv@X)/np.linalg.norm(A_inv@X)
        lam=(np.matmul(v,np.matmul(A_inv,v)))/(np.matmul(v,v))
        X=v

        if abs(lam-lam_prev)/abs(lam)<1E-10:
            break

        lam_prev=lam
    
    return lam,v,k,A


N=[4,16]

for s in N:
    
    print("-"*50)
    print(f"Size of Hilbert Matrix: {s}")
    print()
    E,v,k,A=Power_method_inverse(s,1000)
    val=np.linalg.eigvalsh(A)
    print("Eigenvalue:",1/E)
    print()
    print("Eigenvector:",v)
    print()
    print("Iterations:",k)

    print("Actual min Eigen Value from np:", np.min(val))
    print("Relative Error:",abs(1/E-np.min(val))/np.min(val))
    


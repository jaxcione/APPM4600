import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

mp.mp.dps = 60

def matrix(n):
    H_exact=mp.matrix(n,n)
    for k in range(1,n+1):
        for s in range(1,n+1):
            H_exact[k-1,s-1]=mp.mpf(1)/(k+s-1)

    A=np.empty((n,n),dtype=float)
    for i in range(1,n+1):
        for j in range(1,n+1):
            A[i-1][j-1]=(1)/(i+j-1)

    return A,H_exact

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
    A,H_exact=matrix(n)

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
    
    return lam,v,k,A,H_exact

N=[4,16]
u=np.finfo(float).eps/2

for s in N:
    
    print("-"*50)
    print(f"Size of Hilbert Matrix: {s}")
    print()
    E_inv,v,k,A,H_exact=Power_method_inverse(s,1000)

    #computing error term by term since you cannot do subtraction of matrices with mpf and np 
    H_fl=mp.matrix(s,s)
    E=np.empty((s,s))
    for i in range(s):
        for j in range(s):
            H_fl[i,j]=mp.mpf(float(A[i,j])) #converting A into mp form
            E[i,j]=float(H_fl[i,j]-H_exact[i,j])
    normE=np.linalg.norm(E,2)

    #the eigenvalue of the exact and float hilbert matrixc
    ev_true=mp.eigsy(H_exact,eigvals_only=True) 
    ev_fl=mp.eigsy(H_fl,eigvals_only=True)

    lam_true=ev_true[0]
    for i in range(s):
        if ev_true[i]<lam_true:
            lam_true=ev_true[i]

    mu=ev_fl[0]
    for i in range(s):
        if ev_fl[i]<mu:
            mu=ev_fl[i]


    lam=1/E_inv #actual 

    print("Eigenvalue:",lam)
    print()
    print("Eigenvector:",v)
    print()
    print("Iterations:",k)
    print("|| E ||:",normE)
    print("u||A||:",u*np.linalg.norm(A,2))
    print()
    print("True min Eigen Value:",mp.nstr(lam_true,8))
    print("mu:",mp.nstr(mu,8))
    print("|lambda-mu|:",mp.nstr(abs(lam_true-mu),8))
    print("|lambda-mu|<=||E||:",abs(lam_true-mu)<=normE)

########################################################################
# This python script tests shifted inverse power iteration for finding
# the eigenvalue of a matrix closest to a shift alpha and compares its
# run time to a full eigenvalue solve.
# (equivalent to power_test.m)
# APPM 4600
########################################################################
import time
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm
from scipy.linalg import lu_factor, lu_solve

def driver():

    # fix the random seed so every run gives the same results
    np.random.seed(1)

# example 1
    '''
    n = 1000

    dd = np.ones(n)
    dd[0] = 4000
    dd[1] = 4000-500
    dd[2] = 10   
    '''
# example 2
    '''
    n = 4
# example 3: |3+4i| = |3-4i| = 5, no dominant eigenvalue -> power method fails
#    dd = np.array([-2, 1, 3+4j, 3-4j])
    '''

# example 3
    n = 5   
    dd = np.array([10, 20, 20.001, 80,50] )
    #dd = np.arange(1, n+1)
    
#    print('dd = ', dd)
    
    X = np.random.randn(n, n)

    # X*diag(dd)*inv(X): eigenvalues are the entries of dd
    A = X @ np.diag(dd) @ inv(X)

    # shift: inverse iteration converges to the eigenvalue closest to alpha
    alpha=[]
    delta=np.linspace(0,1-1E-10,11)
    for k in range(0,len(delta)):
        alpha.append(19+delta[k])
    alpha=np.array(alpha)
    for j in range(len(alpha)):
        # target eigenvalue and convergence rate |lambda_1-alpha|/|lambda_2-alpha|
        # where lambda_1, lambda_2 are the closest and second closest to alpha
        dist = np.sort(np.abs(dd - alpha[j]))
        lam1 = dd[np.argmin(np.abs(dd - alpha[j]))]
        rate = dist[0]/dist[1]
        print('target eigenvalue = ', lam1)
        print('rate = ', rate)

        tol = 1e-8
        t = time.perf_counter()
        [lambdas, X] = np.linalg.eig(A)
        print('eig time: %g seconds' % (time.perf_counter() - t))
        print('lambdas = ', lambdas)

        Nmax = 1000 
        t = time.perf_counter()
        [lam, v,it] = shiftInvpowerIt(A,alpha[j], Nmax,tol)
        print('shifted inverse power time: %g seconds' % (time.perf_counter() - t))
        print('shifted inverse power number of iterations:', it)
        print('shifted inverse power: eigenvalue found:', lam[it-1])

        # only keep the iterations actually used
        err = np.abs(lam[:it] - lam1)

        N = np.arange(1, it+1)
        
        [lam2,_, it2, nLU] = restart(A, alpha[j],Nmax,tol,z=0.5)
        print('restarted iterations:',it2,'factorizations:', nLU)
        print('restarted eigenvalue:',lam2[it2-1]) 

        plt.semilogy(N, err, 'o-', label=r'$|\lambda^{(k)} - \lambda_1|$')
        plt.semilogy(N, rate**N, 'r', label=r'$\left(|\lambda_1-\alpha|/|\lambda_2-\alpha|\right)^k$')
        plt.xlabel('iteration $k$')
        plt.ylabel('error')
        plt.title(r'Shifted inverse power iteration, $\alpha = %g$' % alpha[j])
        plt.legend()
        plt.show()


def powerIt(A, Nmax,tol):

    n = A.shape[0]

    q = np.random.rand(n)
    q = q/np.linalg.norm(q)
    lam = np.zeros(Nmax, dtype=complex)

    for j in range(Nmax):
        z = A @ q
        q = z/np.linalg.norm(z)
        lam[j] = np.vdot(q, A @ q)
#        if (np.abs(lam[j]-lam[j-1])/np.abs(lam[j])<tol):
        if (np.abs(lam[j]-lam[j-1])<tol):
           return [lam, q,j+1]

    v = q

    return [lam, v,j+1]

def shiftInvpowerIt(A,alpha, Nmax,tol):

    n = A.shape[0]

    # factor A - alpha*I once; each iteration is then just two triangular solves
    LU = lu_factor(A-alpha*np.identity(n))
    
#    print('LU = ', LU)

    q = np.random.rand(n)
    q = q/np.linalg.norm(q)
    q0 = q
    lam = np.zeros(Nmax, dtype=complex)
    c=(norm(A,2))

    for j in range(Nmax):
        z = lu_solve(LU, q0)
        q = z/np.linalg.norm(z)
        q1 = q
        # Rayleigh quotient with A (not the inverse) gives the eigenvalue of A
        B=A@q
        lam[j] = np.vdot(q, B)
        if norm(B-lam[j]*q)/c<tol:
#        if (j > 0 and norm(q1-q0)<tol):
           return [lam, q,j+1]
        q0=q1   
#        if (j > 0 and np.abs(lam[j]-lam[j-1])<tol):
#           return [lam, q,j+1]

    v = q

    return [lam, v,j+1]

def restart(A,alpha,Nmax,tol,z=.5):
    norm_A=norm(A,2)
    n=A.shape[0]
    
    # factor A - alpha*I once; each iteration is then just two triangular solves
    LU =lu_factor(A-alpha*np.identity(n))
    shift=0
    q = np.random.rand(n)
    q = q/np.linalg.norm(q)
    lam = np.zeros(Nmax, dtype=complex)
    
    for j in range(Nmax):
        z=lu_solve(LU, q)
        q=z/np.linalg.norm(z)
        B=A@q
        lam[j] = np.vdot(q,B)
        
        if np.linalg.norm(B-lam[j]*q)/(norm_A) < tol:
            return [lam,q,j+1,nLU]

        if j-shift>=2:
            d1 = np.abs(lam[j]-lam[j-1])
            d0 = np.abs(lam[j-1]-lam[j-2])
            if d0 > 0 and d1/d0 >z:
                alpha = lam[j].real         
                LU =lu_factor(A-alpha*np.identity(n))
                nLU+= 1
                shift=j+1            

    return [lam, q, Nmax, nLU]

driver()

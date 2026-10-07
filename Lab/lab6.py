import numpy as np
import matplotlib.pyplot as plt

#prelab-----------------------------------

def evalF(x):
    F=np.zeros(2)
    F[0]=(x[0]**2)+(x[1]**2)-2
    F[1]=(np.exp(x[0]-1))+(x[1]**2)-2
    return F

def evalJ(x):
    J=np.zeros((2,2))
    J[0,0]=2*x[0]
    J[0,1]=2*x[1]
    J[1,0]=np.exp(x[0]-1)
    J[1,1]=2*x[1]
    return J

def Newton(x0, tol, Nmax):
    """
    inputs: x0 = initial guess, tol = tolerance, Nmax = max its
    Outputs: xstar = approx root, ier = error message, its = num its
    """
    for its in range(Nmax):
        J = evalJ(x0)
        Jinv = np.linalg.inv(J)
        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)
        if np.linalg.norm(x1 - x0) < tol:
            xstar = x1
            ier = 0
            return [xstar, ier, its]
        x0 = x1
    
    xstar = x1
    ier = 1
    return [xstar, ier, Nmax]


def LazyNewton(x0, tol, Nmax):
    """
    Lazy Newton = use only the inverse of the Jacobian for initial guess
    inputs: x0 = initial guess, tol = tolerance, Nmax = max its
    Outputs: xstar = approx root, ier = error message, its = num its
    """
    J = evalJ(x0)
    Jinv = np.linalg.inv(J)
    for its in range(Nmax):
        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)
        if np.linalg.norm(x1 - x0) < tol:
            xstar = x1
            ier = 0
            return [xstar, ier, its]
        x0 = x1
    
    xstar = x1
    ier = 1
    return [xstar, ier, Nmax]

x0=np.array([2,5])
x1=np.array([3,5])
eps=1e-6

print(Newton(x0, eps, 100))
print(LazyNewton(x0, eps, 100))

print(Newton(x1, eps, 100))
print(LazyNewton(x1, eps, 100))

#--------------------------------------------------------

#building slacking newton method

def SlackerNewton(x0, tol, Nmax):
   
    J = evalJ(x0)
    Jinv = np.linalg.inv(J)
    err=1E10

    for its in range(Nmax):
        F = g(x0)
        x1 = x0 - Jinv.dot(F)
        v=np.linalg.norm(x1-x0)

        if np.linalg.norm(x1 - x0) < tol:
            xstar = x1
            ier = 0
            return [xstar, ier, its]
        
        
        x0 = x1

        if v>err: 
                    J=evalJ(x0)
                    Jinv=np.linalg.inv(J)
        err=v

        
    
    xstar = x1
    ier = 1
    return [xstar, ier, Nmax]


def g(x):
    return np.array([4*x[0]**2+4*x[1]**2-4,x[0]+x[1]-np.sin(x[0]-x[1])])

x2=np.array([1,0])
eps2=1E-10

print(SlackerNewton(x2, eps2, 100))



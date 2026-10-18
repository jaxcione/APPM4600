import numpy as np
import matplotlib.pyplot as plt





def f(x):
    return 1/(1+(x)**2)

def Mk(x_eval,y_eval):

    n=len(x_eval)-1 #length of how many points we have
    B=np.zeros((n,n)) #our matrix 
    rhs=np.zeros(n) #rhs of the equation

    h=np.diff(x_eval) #creates an array of te differences 

    #boundary conditions
    B[0,0]=1
    B[n,n]=1
    rhs[0]=0
    rhs=[n]=0

    for k in range(1,n):


        B[k][k-1]=h[k-1]/6
        B[k][k]=(h[k-1]+h[k])/3
        B[k][k+1]=h[k]/6


        rhs[k]=((y_eval[k+1]-y_eval[k])/h[k])-((y_eval[k]-y_eval[k-1])/h[k-1])

    return np.linalg.solve(B,rhs)
            

def cubic_spline(x,x_eval,y_eval):
    pass


x_eval=np.linspace(-5,5,5)
y_eval=np.array([f(xi) for xi in x_eval])
print(Mk(x_eval,y_eval))




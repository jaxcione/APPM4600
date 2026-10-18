import numpy as np
import matplotlib.pyplot as plt





def f(x):
    return 1/(1+(x)**2)

def Mk(x_eval,y_eval):

    n=len(x_eval)-1 #length of how many points we have
    B=np.zeros((n+1,n+1)) #our matrix 
    rhs=np.zeros(n+1) #rhs of the equation

    h=np.diff(x_eval) #creates an array of te differences 

    #boundary conditions
    B[0,0]=1
    B[n,n]=1
    rhs[0]=0
    rhs[n]=0

    for k in range(1,n):


        B[k][k-1]=h[k-1]/6
        B[k][k]=(h[k-1]+h[k])/3
        B[k][k+1]=h[k]/6


        rhs[k]=((y_eval[k+1]-y_eval[k])/h[k])-((y_eval[k]-y_eval[k-1])/h[k-1])

    Mk=np.linalg.solve(B,rhs)

    return Mk
            

def Sk(x,x_eval,y_eval):
    mk=Mk(x_eval,y_eval)
    h=np.diff(x_eval)
    s=0
    for j in range(len(mk)-1):
        c1=mk[j]/(6*h[j])
        c2=mk[j+1]/(6*h[j])
        c3=(y_eval[j]/h[j])-(mk[j]*h[j]/6)
        c4=(y_eval[j+1]/h[j])-(mk[j+1]*h[j]/6)

        s+=c1*(x_eval[j+1]-x)**3+c2*(x-x_eval[j])**3+c3*(x_eval[j+1]-x)+c4*(x-x_eval[j])
    return s

    
x_eval=np.linspace(-5,5,5) 
y_eval=np.array([f(xi) for xi in x_eval])






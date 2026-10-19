import numpy as np
import matplotlib.pyplot as plt

###########################################################
#Natural BC

def f(x):
    return 1/(1+(x)**2)

def Mk(x_eval,y_eval):

    n=len(x_eval)-1 #length of how many points we have
    B=np.zeros((n+1,n+1)) #our matrix 
    rhs=np.zeros(n+1) #rhs of the equation

    h=np.diff(x_eval) #creates an array of te differences 

    #boundary conditions
   

    for k in range(1,n):

        B[k][k-1]=h[k-1]/6
        B[k][k]=(h[k-1]+h[k])/3
        B[k][k+1]=h[k]/6


        rhs[k]=((y_eval[k+1]-y_eval[k])/h[k])-((y_eval[k]-y_eval[k-1])/h[k-1])

    B[0,0]=1
    B[n,n]=1
    rhs[0]=0
    rhs[n]=0
    Mk=np.linalg.solve(B,rhs)

    return Mk
            

def Sk(x,x_eval,y_eval):
    mk=Mk(x_eval,y_eval)
    h=np.diff(x_eval)
    s=0

    j=np.searchsorted(x_eval,x)-1 #sorts what our index is based on x value that is passed through in the loop (xi)
    j=np.clip(j,0,len(h)-1) #clipping it s.t we arent out of bounds

    
    c1=mk[j]/(6*h[j])
    c2=mk[j+1]/(6*h[j])
    c3=(y_eval[j]/h[j])-(mk[j]*h[j]/6)
    c4=(y_eval[j+1]/h[j])-(mk[j+1]*h[j]/6)

    s=c1*(x_eval[j+1]-x)**3+c2*(x-x_eval[j])**3+c3*(x_eval[j+1]-x)+c4*(x-x_eval[j])
    return s

r=20
x_eval=np.linspace(-5,5,r) 
y_eval=f(x_eval)
X=np.linspace(-5,5,1000)
Y=np.array([Sk(xi,x_eval,y_eval) for xi in X]) 

plt.plot(X,f(X),"k--",label="True f(x)")
plt.plot(X,Y,color='purple',label=f'Cubic Spline, N={r}')
plt.legend(loc='upper right')
plt.grid()
plt.show()

#########################################################################################
#clampled bc

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/(1+(x)**2)

def f_prime(x):
    return -2*x/((1+(x**2))**2)


def Mk(x_eval,y_eval):

    n=len(x_eval)-1 #length of how many points we have
    B=np.zeros((n+1,n+1)) #our matrix 
    rhs=np.zeros(n+1) #rhs of the equation

    h=np.diff(x_eval) #creates an array of te differences 

    #boundary conditions
   

    for k in range(1,n):

        B[k][k-1]=h[k-1]/6
        B[k][k]=(h[k-1]+h[k])/3
        B[k][k+1]=h[k]/6


        rhs[k]=((y_eval[k+1]-y_eval[k])/h[k])-((y_eval[k]-y_eval[k-1])/h[k-1])

    B[0,0]=2
    B[0,1]=1
    B[n,n]=2
    B[n,n-1]=1
    rhs[0]=6*((y_eval[1]-y_eval[0])/(h[0]**2))-(6*f_prime(x_eval[0])/h[0])
    rhs[n]=6*((y_eval[n]-y_eval[n-1])/(h[n-1]**2))-(6*f_prime(x_eval[n])/h[n-1])
    Mk=np.linalg.solve(B,rhs)

    return Mk
            

def Sk(x,x_eval,y_eval):
    mk=Mk(x_eval,y_eval)
    h=np.diff(x_eval)
    s=0

    j=np.searchsorted(x_eval,x)-1 #sorts what our index is based on x value that is passed through in the loop (xi)
    j=np.clip(j,0,len(h)-1) #clipping it s.t we arent out of bounds

    
    c1=mk[j]/(6*h[j])
    c2=mk[j+1]/(6*h[j])
    c3=(y_eval[j]/h[j])-(mk[j]*h[j]/6)
    c4=(y_eval[j+1]/h[j])-(mk[j+1]*h[j]/6)

    s=c1*(x_eval[j+1]-x)**3+c2*(x-x_eval[j])**3+c3*(x_eval[j+1]-x)+c4*(x-x_eval[j])
    return s

r=20
x_eval=np.linspace(-5,5,r) 
y_eval=f(x_eval)
X=np.linspace(-5,5,1000)
Y=np.array([Sk(xi,x_eval,y_eval) for xi in X]) 

plt.plot(X,f(X),"k--",label="True f(x)")
plt.plot(X,Y,color='purple',label=f'Cubic Spline, N={r}')
plt.legend(loc='upper right')
plt.grid()
plt.show()




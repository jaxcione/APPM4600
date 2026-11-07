import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x)*np.cos(x)

def traps(a,b,n,tol,h_vals=None,error_vals=None):
     
    if h_vals is None:
               h_vals=np.array([])
    if error_vals is None:
               error_vals=np.array([])

    h=(b-a)/n
    I= -12.070346316389632
    sum_val=h/2*(f(a)+f(b))
 

    for k in range(1,n):
        sum_val+=h*f(a+k*h)

    x=h
    y=abs(sum_val-I)/abs(I)

    h_vals=np.append(h_vals,x)
    error_vals=np.append(error_vals,y)
        

    if abs(sum_val-I)/abs(I)<tol:
        return sum_val,h_vals,error_vals
    else:
        return traps(a,b,2*n,tol,h_vals,error_vals)
    

def simpson(a,b,n,tol,h_vals=None,error_vals=None):

    if h_vals is None:
            h_vals=np.array([])
    if error_vals is None:
            error_vals=np.array([])

    h=(b-a)/n
    sum_val=h/3*(f(a)+f(b))
    I= -12.070346316389632
    
    for k in range(1,int(n/2)):
        sum_val+=(2*h/3)*f(a+(2*k)*h)

    for j in range(0,int(n/2)):
        sum_val+=(4*h/3)*f(a+(2*j+1)*h)

    x=h
    y=abs(sum_val-I)/abs(I)

    h_vals=np.append(h_vals,x)
    error_vals=np.append(error_vals,y)

    if abs(sum_val-I)/abs(I)<tol:
        return sum_val,h_vals,error_vals
    else:
        return simpson(a,b,2*n,tol,h_vals,error_vals)
    

X,Y=simpson(0,np.pi,2,1E-10)[1],simpson(0,np.pi,2,1E-10)[2]
X2,Y2=traps(0,np.pi,2,1E-10)[1],traps(0,np.pi,2,1E-10)[2]

slope_simp=(np.log(Y[-1])-np.log(Y[0]))/(np.log(X[-1])-np.log(X[0]))
slope_traps=(np.log(Y2[-1])-np.log(Y2[0]))/(np.log(X2[-1])-np.log(X2[0]))

print("Slope of Simpson:",slope_simp)
print("Slope of Trapezoidal:",slope_traps)
plt.loglog(X,Y,label='Simpsons',color="purple")
plt.loglog(X2,Y2,label="Trapezoidal",color="green")
plt.legend()
plt.show()


#print("Trapezoidal: ",traps(0,np.pi,2,1E-10))
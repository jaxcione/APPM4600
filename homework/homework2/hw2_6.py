import numpy as np 
import matplotlib.pyplot as plt 
import math 

def g(x):
    return x-4*np.sin(2*x)-3

x=np.linspace(-2,7.5,1000)


plt.plot(x,g(x),color="purple",label="Plot of: f(x)=x− 4sin(2x)−3")
plt.axhline(0,x[0],x[len(x)-1],color='k',linestyle='--')
plt.ylim(-7,5)
plt.grid()
plt.legend()
plt.show()

#fixed point iteration method
#y is our starting point, n is number of iterations, eps is the tolerance
def sequence(y, n,eps):
     
     if n==0:
          return y,"finished recursion"
     
     x=-np.sin(2*y)+5/4*y-3/4

     if abs(x-y)<eps:
          return x,"Number of Iterations:",1000-n,"Completed"
     else:
          return sequence(x,n-1,eps)

print(sequence(0,1000,1e-10))
print(sequence(-.777,1000,1e-10))
print(sequence(2.4,1000,1e-10))
print(sequence(3,1000,1e-10))
print(sequence(4.3,1000,1e-10))
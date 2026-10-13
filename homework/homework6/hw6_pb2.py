import numpy as np
import matplotlib.pyplot as plt

def f1(z):
    return z[0] ** 2 + z[1] ** 2 - 4

def f2(z):
    return np.exp(z[0])+z[1]-1

def F(z):
    return np.array([f1(z),f2(z)])

def quasi_LazyNewton(x0,eps,Nmax):
    counter=0
    starting=x0
    denominator=(2*x0[0]-(2*x0[1]*np.exp(x0[0])))
    if denominator==0:
        return "Division by zero, invalid input"
    
    inv_coeff=1/denominator
    J_inv = inv_coeff * np.array([[1,-2*x0[1]],[-np.exp(x0[0]),2*x0[0]]])
    
    
    for _ in range(Nmax):
        
        counter+=1
        x1=x0-(J_inv)@F(x0)
        
        if np.linalg.norm(x1-x0)<eps:
            return x1,counter,f"Converged! Starting point:{starting} "
        
        x0=x1
        
    return x1,counter, "Did not meet eps criteria"


def quasi_Broyden(x0,eps,Nmax):
      counter=0
      starting=x0
      
      denominator=(2*x0[0]-(2*x0[1]*np.exp(x0[0])))
      if denominator==0:
            return "Division by zero, invalid input"
                  
      
      G=np.array([[2*x0[0], 2*x0[1]], [np.exp(x0[0]), 1]])
      
      for _ in range(Nmax): 
          counter+=1
          x1=x0-np.linalg.inv(G)@F(x0)
          
          if np.linalg.norm(x1-x0)<eps:
                      return x1,counter,f"Converged! Starting point:{starting} "
          x_new=(F(x1)-F(x0))-G@(x1-x0)
          y_new=(x1-x0)/(np.linalg.norm(x1-x0)**2)
          
          G+=np.outer(x_new,y_new)
          x0=x1
          
      return x1,counter, "Did not meet eps criteria"
    

w1=np.array([1,1])
w2=np.array([1,-1])
w3=np.array([0.001,0.001])

print("Lazy Newtons")
print(quasi_LazyNewton(w1,10**-4,1000))
print(quasi_LazyNewton(w2,10**-4,1000))
print(quasi_LazyNewton(w3,10**-4,1000))
print("------------------------------------------------")
print("Broydens")
print(quasi_Broyden(w1,10**-4,1000))
print(quasi_Broyden(w2,10**-4,1000))
print(quasi_Broyden(w3,10**-4,1000))
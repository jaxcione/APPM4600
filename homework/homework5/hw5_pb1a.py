import numpy as np
import matplotlib.pyplot as plt
import time


def f(x,y):
    return 3*(x**2)-(y**2)

def g(x, y):
    return 3*x*y**2-x**3-1

x0=1
y0=1
matrix=np.array([[1/6,1/18],[0,1/6]])


#iteration method for aprt a
def iteration(x0,y0,matrix,eps):
    p=np.array([f(x0,y0),g(x0,y0)])
    
    counter=0
    while np.linalg.norm(p)>eps:
        counter+=1 #counting number of iterations
        w=np.array([x0,y0]) #setting a vector to be w to store vals
        p=np.array([f(x0,y0),g(x0,y0)]) #function vector 

        coeff=1/((30*(x0**2)*y0)+(6*y0**3)) #coeff of the inverse of J 
        J_inv=coeff*np.array([[6*x0*y0,2*y0],[-3*y0**2+3*x0**2,6*x0]]) #jacovian inverse
        F=w-J_inv@p

        #updatin x0 y0 
        x0=F[0]
        y0=F[1]
           
    return w,counter-1


print(iteration(x0,y0,matrix,1E-10))
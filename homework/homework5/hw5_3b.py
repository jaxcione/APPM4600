import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def F(x):
    return x[0]**2+4*x[1]**2+4*x[2]**2-16

def f_x(x):
    return 2*x[0]

def f_y(x):
    return 8*x[1]

def f_z(x):
    return 8*x[2]

def iteration(x0,tol,max):
    err=[]
    for k in range(max):
        d=F(x0)/(f_x(x0)**2+f_y(x0)**2+f_z(x0)**2)
        x1=x0[0]-d*f_x(x0)
        y1=x0[1]-d*f_y(x0)
        z1=x0[2]-d*f_z(x0)

        err.append(np.linalg.norm(x0-np.array([x1,y1,z1])))
        if np.linalg.norm(x0-np.array([x1,y1,z1]))<tol:
            break
        x0=np.array([x1,y1,z1])

    return x0,err


v=np.array([1,1,1])
print(iteration(v,1e-10,10000000000)[0])
get=(iteration(v,1e-10,100000000000)[1])

alpha=0
counter=0
for j in range(1,len(get)-1):
    if get[j+1]!=0 and get[j]!=0:
        counter+=1
        alpha+=np.log(get[j+1]/get[j])/np.log(get[j]/get[j-1])
    else:
        alpha+=0


print(alpha/counter)

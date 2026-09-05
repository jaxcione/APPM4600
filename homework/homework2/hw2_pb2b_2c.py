import numpy as np 
import matplotlib.pyplot as plt
import math

A=.5*np.array([[1,1],[1+(10**-10),1-(10**-10)]]) #array given in prob
A_TA=A.T@A

print(A_TA)

U,S,V=np.linalg.svd(A) #doing a single value decompoision on A
print("U",U)
print("S",S)
print("V",V) 

K=S[0]/S[1] #grabbing the singular values and calculaing condition number
print("Condition Number",K)

#initializing matrix/vectors
A_inv=np.array([[1-(10**10),10**10],[1+(10**10),-10**10]])
delta_b=np.array([10**-5,2*10**-5])
x=np.array([1,1])


relative_error=np.linalg.norm(A_inv@delta_b)/np.linalg.norm(x)  #taking the relative error
print(relative_error)
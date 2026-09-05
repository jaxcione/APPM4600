import numpy as np 
import matplotlib.pyplot as plt
import math

A=.5*np.array([[1,1],[1+(10**-10),1-(10**-10)]])
A_TA=A.T@A

print(A_TA)

U,S,V=np.linalg.svd(A) #doing a single value decompoision on A
print("U",U)
print("S",S)
print("V",V) 

K=S[0]/S[1] #grabbing the singular values and calculaing condition number
print("Condition Number",K)
import numpy as np 
import matplotlib.pyplot as plt
import math

def Condition_number(arr):
    A=.5*np.array([[1,1],[1+(10**-10),1-(10**-10)]]) #array given in prob
    A_TA=A.T@A

    print(A_TA)

    U,S,V=np.linalg.svd(A) #doing a single value decompoision on A
    print("U",U)
    print("S",S)
    print("V",V) 

    return S[0]/S[1] #grabbing the singular values and calculaing condition number
    

def relative_error(perterbation):
#initializing matrix/vectors
    A_inv=np.array([[1-(10**10),10**10],[1+(10**10),-10**10]])
    x=np.array([1,1])
    b_vec=[10**perterbation,2*10**perterbation]

    return np.linalg.norm(A_inv@b_vec)/np.linalg.norm(x)  #taking the relative error
    

#showing the relation of delta_b(or pertebation vector) as a function of relative error 
x=np.linspace(-10,0,10)
f=[relative_error(k) for k in x]
plt.plot(x,f, color='purple')
plt.xlabel("Perterbation (k): x^k where k∈[-10,0]")
plt.ylabel("Relative Error")
plt.yscale("log")
plt.title("Relative Error versus pertabation")
plt.show()

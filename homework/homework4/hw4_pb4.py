import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def f(x):
    return x**6-x-1

def f_prime(x):
    return 6*(x**5)-1

def Newtons(x0,error,eps=10**-13,z=0,counter=0):
    if f_prime(x0)==0:
        return "Dividing by zero error"
    
    x=x0-(f(x0)/f_prime(x0))#our recursive statement

    if abs(x-z)/abs(x)>eps: #relative error is less than 10**-13
        error.append(x)
        z=x
        counter+=1
        return Newtons(x,error,eps=10**-13,z=z,counter=counter)
    else: 
        return x,f"Iterations:{counter}",error


x0_newtons=2
store=[]

newton_result=Newtons(x0_newtons, store, 10**-13, z=0, counter=0)
print("Newtons:", newton_result[:2])
grab = newton_result[2]

def secant(x0,x1,error,eps,counter=0):
    
    if abs(x1-x0)/abs(x1)<eps:
        return x1,f"Iterations:{counter}",error
    f0=f(x0)
    f1=f(x1)
    
    if x1-x0==0:
        return "Division by zero"
    if f(x1)-f(x0)==0:
            return "Division by zero"
        
        
    m=(f1-f0)/(x1-x0)

    x=x1-f1/m
    
    counter+=1
    error.append(x)

    
    return secant(x1,x,error,eps,counter=counter,)

x0,x1=2,1

error_secant=[]
secant_result = secant(x0, x1, error_secant, 10**-13, counter=0)
print("Secant:", secant_result[:2])
grab2 = secant_result[2]

print("Newton List:",pd.DataFrame(grab))
print("Secant List:",pd.DataFrame(grab2))





alpha = newton_result[0]  # Exact root approximation

arr_n=np.array(grab)
en_k = np.abs(arr_n[:-1] - alpha)
en_k1 = np.abs(arr_n[1:]-alpha)

arr_s=np.array(grab2)
es_k = np.abs(arr_s[:-1] - alpha) #grabbing all values but the last
es_k1 = np.abs(arr_s[1:] - alpha) #all values but the first 

plt.figure(figsize=(8, 6))
plt.loglog(en_k, en_k1,marker="o",color="purple",linestyle=":" ,markersize=4,label="Newton's Method")
plt.loglog(es_k, es_k1,marker="o",color="green",linestyle=":", markersize=4,label="Secant Method")
plt.xlabel("|x_k - alpha|")
plt.ylabel("|x_{k+1} - alpha|")
plt.title("Log-Log Error Convergence")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.show()
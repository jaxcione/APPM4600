import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.special 


alpha=0.138*10**-6
T_s=-15
T_i=20
t=60*3600*24
e=10**-3

m=2*np.sqrt(alpha*t)


def f(x):
    return scipy.special.erf(x/m)-15/35

x_bar=3
x_vec=np.linspace(0,x_bar,1000)

plt.plot(x_vec,f(x_vec),color='purple',label=f"Plot of: f(x)=erf(x/m)-15/35")
plt.xlabel("x")
plt.hlines(0,0,3,colors='k',linestyles='--')
plt.ylabel("f(x)")
plt.legend()
plt.show()
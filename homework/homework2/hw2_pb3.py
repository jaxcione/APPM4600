import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import math

#part b-----------------------------------------------
def F(x):
    y=math.exp(x)
    return y-1
perterbations=np.arange(-.0000001,.0000001,10**-9)
y=[F(k) for k in perterbations]

for i, val in enumerate(perterbations):
    print(f"Perturbation {i}: {val}, F(x): {y[i]}")

#------------------------------------------------------
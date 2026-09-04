import numpy as np
import matplotlib.pyplot as plt


z=np.arange(1.920,2.080,.001)

def p(x):
    return x**9 - 18*x**8 + 144*x**7 - 672*x**6 + 2016*x**5 - 4032*x**4 + 5376*x**3 - 4608*x**2 + 2304*x - 512

def p2(x):
    return (x-2)**9


y1=p(z)
y2=p2(z)

plt.plot(z,y1,label="P(x)")
plt.plot(z,y2,label="(x-2)^9")
plt.legend()
plt.show()
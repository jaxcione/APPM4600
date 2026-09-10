import numpy as np

def fixed(m,alpha,sequence):
    pass

def fixed_point(v,N):
    x=np.zeros((N,1))
    x[0]=v
    for n in range(len(v)):
        fixed_point=fixed(x[n])

    return x
import numpy as np

alpha=2
def fixed_point(N,alpha,sequence):
    x=np.zeros((N,1))
    x[0]=sequence
    for n in range(len(m-1)):
        x[n+1]=alpha(x[n])

    return x

def fixed(v,N,p):
    x=fixed_point(N,alpha,v)
    error=np.abs(x-p)
    
    q=np.log



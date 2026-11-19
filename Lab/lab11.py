import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x

def composite_trap(a,b,N):
    h=(b-a)/N
    sum=h/2*(f(a)+f(b))

    for k in range(1,N-1):
        sum+=h*f(a+k*h)
        
    return sum


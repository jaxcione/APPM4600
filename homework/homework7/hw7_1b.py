import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (1 + (10*x) ** 2) **(-1)

def A(x,N):
    M=np.zeros((N,N),dtype=float)
    for k in range(N):
        for j in range(N):
            M[k][j]=x[k]**(N-(j+1))
            
    return M
            
def C(N):
    x0=[]
    for i in range(1,N+1):
        x0.append(-1+(2*(i-1))/(N-1)) #x0 vector
    x0=np.array(x0)

    V0=A(x0,N)
    c0=np.linalg.solve(V0,f(x0))

    return c0

def polynomial(x,c,N):
    p=0
    for i in range(N):
        p+=c[i]*x**(N-(i+1))
    return p

def Plotting(N, colors):
    for N in N_vec:

        c_=C(N)
        if max(np.abs(polynomial(np.linspace(-1,1,100),c_,N)))<=100:

            plt.plot(np.linspace(-1,1,100),polynomial(np.linspace(-1,1,100),c_,N),marker='o',markersize=3,linestyle='solid',color=colors[N%len(colors)],label=f"P(x),N={N}")
            plt.plot(x_f,f(x_f),label='f(x)',color='black',linestyle='dashed')
            plt.xlim(-1,1)
            plt.ylim(0,1.1)
            plt.legend()
            plt.show()
        else:
            break

N_vec=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x_f=np.linspace(-1,1,1001)
colors=['blue','orange','green','red','purple','brown','pink','gray','olive','cyan','brown','blueviolet',
        'darkorange','darkgreen','darkred','darkblue','darkcyan','darkmagenta','gold','lightcoral']

Plotting(N_vec,colors)

    


   

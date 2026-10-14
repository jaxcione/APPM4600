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
        y=np.cos((2*(i-1)*np.pi)/(2*N))
        #z=-1+(2*(i-1))/(N-1)
        x0.append(y) #x0 vector
    x0=np.array(x0) #making it an numpy array s.t we can use it to solve the system of eq 

    V0=A(x0,N)
    c0=np.linalg.solve(V0,f(x0)) #solving for coeff

    return c0

#creating a polynomial function using our c 
def polynomial(x,c,N):
    p=0
    for i in range(N):
        p+=c[i]*x**(N-(i+1))
    return p

def Plotting(N, colors):
    for N in N_vec:

        c_=C(N)
        

        plt.plot(np.linspace(-1,1,100),polynomial(np.linspace(-1,1,100),c_,N),marker='o',markersize=3,linestyle='solid',color=colors[N%len(colors)],label=f"P(x),N={N}")
        plt.plot(x_f,f(x_f),label='f(x)',color='black',linestyle='dashed')
        plt.xlim(-1,1)
        plt.ylim(0,1.1)
        plt.legend()
        plt.show()
        

N_vec=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,40,60]
x_f=np.linspace(-1,1,1001)
colors=['blue','orange','green','red','purple','brown','pink','gray','olive','cyan','brown','blueviolet',
        'darkorange','darkgreen','darkred','darkblue','darkcyan','darkmagenta','lightcoral','brown','red']

Plotting(N_vec,colors)

    


   

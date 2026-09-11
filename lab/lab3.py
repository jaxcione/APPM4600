import numpy as np 

#before lab

def fixed_point_calc(n,x0,sequence):

    z=x0 #setting as our original point

    for _ in range(0,n): #doing the sequence n times
        z=sequence(z)
    return z



def vec_iterator(vector,sequence,x0):
    N=len(vector)
    x=np.zeros((N,1)) #filling w N zeros 
    counter=0 #starting the counter at 0

    for k in range(len(x)):
        x[k]=fixed_point_calc(counter,x0,sequence) #calling it for counter number of times 
        counter+=1

    return x #returning our array

#exercise 2.2.1---------------------------------------------------------------------------------------

# we can estimate the order of convergence by doing ln(ek/ek-1)/ln(ek/ek-1)
m=np.arange(100)
g1=lambda x:np.cos(x) #some random sequence tbh
P=0.7390851332151607 #our fixed point 
alpha=[]


y=vec_iterator(m,g1,1)


def obtain_alpha(P,vector):
    e=np.abs(vector-P)
    alpha=[]
    for j in range(1,len(e)-1):
        if e[j-1]==0 or e[j]==0 or np.log(e[j]/e[j-1])==0:
            continue
        else:
            alpha.append(np.log(e[j+1]/e[j])/np.log(e[j]/e[j-1])) #appendign it so we can see it converge 
    return alpha
#Exercise 2.2.2----------------------------------------------

g2= lambda z: (10/(z+4))**1/2
p0=1.5
eps=10**-10
P2=.365230013414097

l=vec_iterator(m,g2,p0)
alpha2=obtain_alpha(P2,l)
print(alpha2[len(alpha2)-1]) #converges to 0. Hence our convergence rate for g2 is better than linear 
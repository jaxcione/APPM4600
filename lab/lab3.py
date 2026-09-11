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
m=np.arange(50)
g1=lambda x:np.cos(x) #some random sequence tbh
P=0.7390851332151607 #our fixed point 
alpha=[]


y=vec_iterator(m,g1,1)
e=np.abs(y-P)

for j in range(1,len(e)-1):
    if e[j-1]==0 or e[j]==0 or np.log(e[j]/e[j-1])==0:
        continue
    else:
        alpha.append(np.log(e[j+1]/e[j])/np.log(e[j]/e[j-1])) #appendign it so we can see it converge 
print(alpha[len(alpha)-1]) #printing the last value of alpha to see if it converges to 1

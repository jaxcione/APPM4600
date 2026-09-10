import numpy as np 
import matplotlib.pyplot as plt


def original(x,d): #original is the function given within the problem
    return np.cos(x+d)-np.cos(x)

def new(x,d): #using a trig identity we can rewwrite the function to avoid cancellation error
    return -2*np.sin((2*x+d)/2)*np.sin(d/2)

delta_vec=10**(-np.linspace(16,0,17)) #vector 10^-16-->10^0
x1=np.pi
x2=10**6

def difference(x,d,func,og): #calcualting the dfference 
    return abs(func(x,d)-og(x,d))


#plotting the difference of orignal and new functions for same x values
plt.semilogx(delta_vec,difference(x1,delta_vec,new,original),color='red',linestyle="--",label="x=π")
plt.semilogx(delta_vec,difference(x2,delta_vec,new,original),color='purple',linestyle="-",label="x=10^6")
plt.title("Difference of the functions")
plt.xlabel("delta")
plt.ylabel("Difference")
plt.legend()
plt.show()


def Taylor(x,d):
    return -d*np.sin(x)-(d**2)/2*np.cos(x)

#doing the same thing for taylor expansion and comparing it to the other functions
plt.semilogx(delta_vec,difference(x1,delta_vec,Taylor,original),color="#FA6970",linestyle="--",label="Taylor-Original, x=π")
plt.semilogx(delta_vec,difference(x2,delta_vec,Taylor,original),color='purple',linestyle="-",label="Taylor-Original, x=10^6")
plt.semilogx(delta_vec,difference(x1,delta_vec,new,original),color='brown',linestyle="--",label="New-Original, x=π")
plt.semilogx(delta_vec,difference(x2,delta_vec,new,original),color="#009E73",linestyle="-",label="New-Original, x=10^6")
plt.semilogx(delta_vec,difference(x1,delta_vec,Taylor,new),color="#0072B2",linestyle="--",label="Taylor-New, x=π")
plt.semilogx(delta_vec,difference(x2,delta_vec,Taylor,new),color="#E667DF",linestyle="--",label="Taylor-New, x=10^6")
plt.xlabel("delta")
plt.ylabel("Difference of Taylor/Rearranged-Original")
plt.title("Difference of the functions")
plt.legend()
plt.show()

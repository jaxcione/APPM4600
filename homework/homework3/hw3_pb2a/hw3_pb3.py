import numpy as np
import matplotlib.pyplot as plt 

#all the functions and their derivitives. I just calcuated their dervives from a derivive calc online. Im too lazy lol
#---------------------------------
def f_1(x):
    return x*(1+(7-x**5)/x**2)**3

def f_1_prime(x):
    g=1+(7-x**5)/x**2
    gp=-3*x**2-14/x**3
    return g**3+3*x*g**2*gp

def f_2(x):
    return x-(x**5-7)/x**2

def f_2_prime(x):
    return 1-3*x**2-14/x**3

def f_3(x):
    return x-(x**5-7)/(5*x**4)

def f_3_prime(x):
    return 4/5-28/(5*x**5)

def f_4(x):
    return x-(x**5-7)/12

def f_4_prime(x):
    return 1-(5*x**4)/12

#---------------------------------------

#for function mapping 
functions={
    1:f_1,
    2:f_2,
    3:f_3,
    4:f_4 
}

#mapping of derivs
function_deriv={
    1:f_1_prime,
    2:f_2_prime,
    3:f_3_prime,
    4:f_4_prime 
}


#doing fixed_point recurssiuvly 
def fixed_point(m,x0,eps,z=0,counter=0):
    x=functions[m](x0)
    if counter>10000:
        return "Cannot Converge"
    if abs(x-z)/abs(x)>eps:
        counter+=1
        z=x
        return fixed_point(m,x,eps,z,counter)
    else:
        return x
    
    
        
    
 
 
#printing functions evaluated at 7^1/5 and their derivitives------------
l=7**(1/5)
print("F_1(x) at 7^1/5",f_1(l))
print("F_2(x) at 7^1/5",f_2(l))
print("F_3(x) at 7^1/5",f_3(l))
print("F_4(x) at 7^1/5",f_4(l))

print("F_1_prime(x) at 7^1/5",f_1_prime(l))
print("F_2_prime(x) at 7^1/5",f_2_prime(l))
print("F_3_prime(x) at 7^1/5",f_3_prime(l))
print("F_4_prime(x) at 7^1/5",f_4_prime(l))


#this is doing the iterations 
#--------------------
x_naught=1 
epsilon=10**-10  
# print ("Fixed Point iteration for F1(x)",fixed_point(1,x_naught,epsilon,z=0,counter=0))
# print ("Fixed Point iteration for F2(x)",fixed_point(2,x_naught,epsilon,z=0,counter=0))
print ("Fixed Point iteration for F3(x)",fixed_point(3,x_naught,epsilon,z=0,counter=0))
print ("Fixed Point iteration for F4(x)",fixed_point(4,x_naught,epsilon,z=0,counter=0))
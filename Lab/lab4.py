import numpy as np

#looking at newtons method. we want to have g'(x)<1. So letting g(x)=x-f(x)/f'(x)
#we get that |f(x)f''(x)/f'(x)^2|<1

def checker(func,deriv,second_deriv,point):
    if deriv(point)==0:
        return "cannot divide by zero"
        
    val=abs(func(point)*second_deriv(point)/(deriv(point)**2))

    if val<1:
        return True
    else:
        return False
        


def bisection(f,f_prime,a,b,eps=10**-13):
    if f(a)==0:
        return a 
    if f(b)==0:
        return 0
    if f(a)*f(b)>0:
        return None
    

    d=1/2*(a+b)
    if f_prime(d)<1:
        return "You are in the basin"
    fa=f(a)
    fd=f(d)

    while abs(a-d)/(abs(d))>eps:
        d=1/2*(a+b)
        if f_prime(d)<1:
                return "You are in the basin"
        if f(d)*f(a)==0:
            return d 
        if f(d)*f(a)>0:
            a=d
            fa=fd
        else:
            b=d
            fb=fd
        d=1/2*(a+b)
        if f_prime(d)<1:
                return "You are in the basin"

    return d

#part 3.3
# i did have to change the input of the bisection method. I now needed to input f' and f to make it arbitrary 

#here we can let x0=d from newtons
def Netwons(f_prime,x0,eps=10**-13,z=0):
    if f_prime(x0)==0:
        return "Dividing by zero error"
    
    x=x0-(f(x0)/f_prime(x0))#our recursive statement

    

    if abs(x-z)/abs(x)>eps: #relative error is less than 10**-13
        z=x
        return Netwons(x,eps=10**-13,z=z)
    else: 
        return x
    

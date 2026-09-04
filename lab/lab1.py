import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x1=[1,2,3]
print(3*x1) #this prints [1, 2, 3, 1, 2, 3, 1, 2, 3]

y1=np.array([1,2,3])
print(3*y1) #prints (3,6,9)
print('this is 3y',3*y1)

#plotting---------------------------------------

X=np.linspace(0,2*np.pi,100) #partitions from 0,2*pi with 100 points. The size of X is 100
Ya=np.sin(X)
Yb=np.cos(X)

plt.plot(X,Ya)
plt.plot(X,Yb)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


#Exercises 3.2: The basics-------------------------

#1
x2=np.linspace(0,1,10) #goes from 0 to 1 with 10 data points
y2=np.arange(0,1,.1) #goes from 0 to 1 with .1 step size
print('Length of x:',len(x2), 'Length of y:',len(y2)) #prints 10 for each one

#2,3
obtain_3=[x2[0],x2[1],x2[2]]
print('first three entries of x are:', obtain_3)

#4
w=10**(-np.linspace(1,10,10)) #the entries of w are 10^i where i goes from 1 to 10
x3=np.arange(1,len(w)+1,1)
X_new=np.linspace(1,10,10)
print(x3)

#plotting a semilogy--> log in y, linear in x
plt.semilogy(x3,w,label='w')
plt.title(' W Semilogy plot')
plt.legend()#shows the labels
plt.show()

#plotting a semilogy x versus s
s=3*w
plt.semilogy(x3,w,label='w')
plt.semilogy(x3,s,label='s')
plt.title('W and S Semilogy plot')
plt.legend() #shows the labels
plt.show()


#Exercise 4: -----------------------------
def driver():
    n = 100
    x = np.linspace(0,np.pi,n)
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.

    #note these are orthogonal
    f = lambda x: np.sin(x)
    g = lambda x: -np.cos(x)
    y = f(x)
    w = g(x)
    # evaluate the dot product of y and w
    dp = dotProduct(y,w,n)
    # print the output
    print("the dot product is : ", dp)
    return


def dotProduct(x,y,n):
    # Computes the dot product of the n x 1 vectors x and y
    dp = 0
    for j in range(n):
        dp = dp + x[j]*y[j]
    return dp


driver()#calling driver


#does C*A this works for any matrix
def Matrix_Calc(C,A):
    #A is our matrix/vector C is either a vector or matrix
    B=[[0 for _ in range(len(A[0]))] for _ in range(len(C))] #this is a 2D array of zeros with the same dimensions as the output matrix
    i=0
    for row in C: #going through the rows
        for j in range(len(A[0])): #going through the coluns
            B[i][j]=dotProduct(A[:,j],row,len(A[:,j]))
        i+=1
    return B

s2 = np.array([[1, 2]])
P=np.array([[1,0],[2,3]])

s_np = np.array(s2)
P_np = np.array(P)

print("Normal",Matrix_Calc(s2,P))
print("NumPy",s_np@P_np)

#for larger matrirces, the numpy method is much faster and more efficient than the for loop method.

C=np.array([[1,1,1],[4,5,6],[7,8,9]])
w=np.array([[4,5,6]])
print("Normal for larger matrices: ",Matrix_Calc(w,C))
print("Numpy for larger matrices,",w@C)


Val=np.matmul(C,w) #this is the commands built into nump
print(Val)
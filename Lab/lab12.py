#############################################
"""
Copyright (C) 2025 Adrianna M. Gillman
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""


#first to solve for QR factorization, you need to decompose A into an orthogonal matrix Q and an upper triangular martix R
#With this QQ^T=I. To find Q we use gram-scmidt where we use the column space of A to as our first vector. Since A=QR we can multiply 
#by Q^T to get R-->R=Q^TA

#############################################
import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la
import scipy.linalg as scila
import time



def driver():
    ''' create matrix for testing different ways of solving a square
    linear system'''
    ''' N = size of system'''
    N = 100
    
    ''' Right hand side'''
    b = np.random.rand(N, 1)
    A = np.random.rand(N, N)
    
    
    
    #time it takes to construct LU factorization 
    start1=time.perf_counter() 
    
    lu,n=scila.lu_factor(A)
    
    end1=time.perf_counter()
    
    Time_elapsed1=end1-start1
    
    
    start2=time.perf_counter()
    x = scila.lu_solve((lu,n), b)
    end2=time.perf_counter()
    
    Time_elapsed2=end2-start2
    Tot_time=Time_elapsed1+Time_elapsed2
    start3=time.perf_counter()
    x=scila.solve(A,b)
    end3=time.perf_counter()
    
    Time_elapsed3=end3-start3
    
    test = np.matmul(A, x)
    r = la.norm(test - b)
    print(r)
    print("Time elapsed 1:",Time_elapsed1)
    print("Time elapsed 2:",Time_elapsed2)
    print("Time elapsed normal solver",Time_elapsed3)
    print("Total time elapsed LU",Tot_time)

    ''' Create an ill-conditioned rectangular matrix '''
    N = 10
    M = 5
    A = create_rect(N, M)
    b = np.random.rand(N, 1)


def create_rect(N, M):
    ''' this subroutine creates an ill-conditioned rectangular matrix'''
    a = np.linspace(1, 10, M)
    d = 10**(-a)
    D2 = np.zeros((N, M))
    for j in range(0, M):
        D2[j, j] = d[j]
    
    

    ''' create matrices needed to manufacture the low rank matrix'''
    A = np.random.rand(N, N)
    Q1, R = la.qr(A)
    test = np.matmul(Q1, R)
    A = np.random.rand(M, M)
    Q2, R = la.qr(A)
    test = np.matmul(Q2, R)
    B = np.matmul(Q1, D2)
    B = np.matmul(B, Q2)
    return B


if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver()
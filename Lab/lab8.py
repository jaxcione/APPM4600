import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv

#PRELAB

def slope(x0,f0,f1,x1,alpha):
    num=f1-f0
    denom=x1-x0

    if denom==0:
        return "Invalid"
    else:
        m=num/denom
        return f0+m*(alpha-x0)

##########################################################
def f(x):
    return (1 + (10*x) ** 2) **(-1)


    
"""
This script provides you the opportunity to insert your own line evaluator.
You will practice some python skills while getting a better understanding of
how splines work.
"""
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
#############################################


def driver():
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval = np.linspace(a, b, Neval)
    ''' number of intervals'''
    Nint = 10
    '''evaluate the linear spline'''
    yeval = eval_lin_spline(xeval, Neval, a, b, f, Nint)
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
    
    plt.plot(xeval, fex, 'ro-', label='exact function')
    plt.plot(xeval, yeval, 'bs--', label='linear spline')
    plt.legend()
    plt.show()
    
    err = abs(yeval - fex)
    plt.figure()
    plt.semilogy(xeval, err, 'ro--', label='absolute error')
    plt.legend()
    plt.show()

def eval_lin_spline(xeval, Neval, a, b, f, Nint):
    '''create the intervals for piecewise approximations'''
    xint = np.linspace(a, b, Nint + 1)
    '''create vector to store the evaluation of the linear splines'''
    yeval = np.zeros(Neval)
    
    for jint in range(Nint):
        '''find indices of xeval in interval (xint[jint], xint[jint+1])'''
        a1 = xint[jint]
        fa1 = f(a1)
        b1 = xint[jint + 1]
        fb1 = f(b1)
        
        # Find indices of xeval in the current interval
        if jint == Nint - 1:
            ind = np.where((xeval >= a1) & (xeval <= b1))[0]
        else:
            ind = np.where((xeval >= a1) & (xeval < b1))[0]
            
        n = len(ind)
        
        for kk in range(n):
            '''use your line evaluator to evaluate the lines at each of the points in the interval'''
            idx = ind[kk]
            yeval[idx] = slope(a1, fa1, b1, fb1, xeval[idx])
            
    return yeval

if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver()






from numpy.linalg import inv
from numpy.linalg import norm

def driver():
    f = lambda x: np.exp(x)
    a = 0
    b = 1
    ''' number of intervals'''
    Nint = 3
    xint = np.linspace(a, b, Nint+1)
    yint = f(xint)
    ''' create points you want to evaluate at'''
    Neval = 100
    xeval = np.linspace(xint[0], xint[Nint], Neval+1)
    
    # 1 & 2. Create the coefficients and solve for M for the natural spline
    (M, C, D) = create_natural_spline(yint, xint, Nint)
    
    # evaluate the cubic spline
    yeval = eval_cubic_spline(xeval, Neval, xint, Nint, M, C, D)
    
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
    nerr = norm(fex - yeval)
    print('nerr = ', nerr)
    
    plt.figure()
    plt.plot(xeval, fex, 'ro-', label='exact function')
    plt.plot(xeval, yeval, 'bs--', label='natural spline')
    plt.legend()
    plt.show()
    
    err = abs(yeval - fex)
    plt.figure()
    plt.semilogy(xeval, err, 'ro--', label='absolute error')
    plt.legend()
    plt.show()

def create_natural_spline(yint, xint, N):
    # Interval lengths
    h = np.zeros(N)
    for i in range(N):
        h[i] = xint[i+1] - xint[i]
        
    # create the right hand side for the linear system
    b = np.zeros(N+1)
    for i in range(1, N):
        b[i] = (3.0 / h[i]) * (yint[i+1] - yint[i]) - (3.0 / h[i-1]) * (yint[i] - yint[i-1])
        
    # create the matrix A so you can solve for the M values
    A = np.zeros((N+1, N+1))
    A[0, 0] = 1.0
    A[N, N] = 1.0
    
    for i in range(1, N):
        A[i, i-1] = h[i-1]
        A[i, i] = 2.0 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        
    # Invert A using numpy.linalg.inv
    Ainv = inv(A)
    
    # solver for M
    M = np.dot(Ainv, b)
    
    # 3. Create the linear/cubic coefficients C and D
    C = np.zeros(N)
    D = np.zeros(N)
    for j in range(N):
        C[j] = (yint[j+1] - yint[j]) / h[j] - h[j] * (2.0 * M[j] + M[j+1]) / 6.0
        D[j] = (M[j+1] - M[j]) / (6.0 * h[j])
        
    return (M, C, D)

def eval_local_spline(xeval, xi, xip, Mi, Mip, C, D):
    # 4. Evaluates the local cubic spline on subinterval [xi, xip]
    hi = xip - xi
    dx = xeval - xi
    # Using the standard cubic polynomial representation: S(x) = y_i + C*dx + (Mi/2)*dx^2 + D*dx^3
    # Here we evaluate using the standard cubic formulation directly from interval endpoints and moments:
    yi = f_val_at_xi = (Mip * (dx ** 3) + Mi * ((xip - xeval) ** 3)) / (6.0 * hi) + \
                       ((np.exp(xip) / hi) - (hi * Mip / 6.0)) * dx + \
                       ((np.exp(xi) / hi) - (hi * Mi / 6.0)) * (xip - xeval)
    # Alternatively, using C and D coefficients directly:
    # yeval = y_i + C * dx + (Mi / 2.0) * (dx ** 2) + D * (dx ** 3)
    return yi

def eval_cubic_spline(xeval, Neval, xint, Nint, M, C, D):
    yeval = np.zeros(Neval+1)
    for j in range(Nint):
        atmp = xint[j]
        btmp = xint[j+1]
        # find indices of values of xeval in the interval
        ind = np.where((xeval >= atmp) & (xeval <= btmp))[0]
        if len(ind) > 0:
            xloc = xeval[ind]
            # evaluate the spline
            yloc = eval_local_spline(xloc, atmp, btmp, M[j], M[j+1], C[j], D[j])
            # copy into yeval
            yeval[ind] = yloc
    return yeval

if __name__ == '__main__':
    driver()
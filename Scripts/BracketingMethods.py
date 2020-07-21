# -*- coding: utf-8 -*-
"""
Description: 
Demonstrates examples of bracketing methods
1) Graphically
    - A simple method for estimating the root of the equation f(x)=0 is to
      plot the function and see where it crosses the x axis. This point provides 
      a rough approximation of the root.
      
2) Bisection Method
    - When a root is present there is typically a positive and negative side to the left and right. Since
    the two sides are opposite signs if you multiply them they should be negative 
    f(X_lower) * f(X_upper) < 0. If this is the case then there is atleast one real root
    and it is between X_lower and X_upper. The interval between the two X-values are then 
    divided in half and then substituted into the given equation. If the function is zero
    then the root is found, if not then the process is repeated until the error is small.
    
3) False-Position Method (linear interpolation)    
    - This is similar to the Bisection Method but utilizes a linear connection between the
    upper and lower X-values. The X-values are connected by a straight line and the intersection of 
    that line with the X-axis is the resultant X-value and plugged into the equation to. This is repeated
    until the resultant x-value converges on a point.
    
"""

import math
import numpy as np
import matplotlib.pyplot as plt


#Given Equation: ln(x) = 0.70
def F(x): 
    value = math.log(x) - 0.7
    return value
#Givens
X_lower = 1.0
X_upper = 3.0

X_lower2 = 1.0
X_upper2 = 3.0
N = 10
#==============================================================================


#  Graphically
xvalues = np.linspace(X_lower,X_upper,N)
yvalues = []
for n in xvalues:
   fx = F(n)#math.log(n) - 0.7
   yvalues = yvalues + [fx]

solx = math.e**0.7   
plt.plot()   
plt.plot(xvalues,yvalues,'r-',solx,0,'bs')  
plt.axhline(y=0, xmin=0, xmax=1.0) #X-Axis
plt.title('Graphical Method')
plt.show()



#Bisection Method
F_lower = F(X_lower)
F_upper = F(X_upper)  
n = 0 # initialize the counter
error = abs(X_upper-X_lower) # initialize the error   
Tol = 10**-5
while error > Tol:
           n += 1
           BM_estimate = ( X_lower + X_upper ) / 2
           F_estimate = F(BM_estimate)
           
           if( F_estimate == 0 ):        
               print('Got lucky! root =',BM_estimate,' F(r)=',F_estimate)
               print(' in',n,' tries',' error <=',error/2)             
               break
           elif( F_lower*F_estimate < 0 ):
               X_upper = BM_estimate
               F_upper = F_estimate
               
           else:
               X_lower = BM_estimate
               F_lower = F_estimate
           
           error = error/2 
           if error == 0:
               break
print("\nBisection Method Iterations: ",n)
print("Bisection Method Estimate: ",BM_estimate)

error = abs(X_upper-X_lower)


# False position
F_lower2 = F(X_lower2)
F_upper2 = F(X_upper2)  
n2 = 0 # initialize the counter
error2 = abs(X_upper-X_lower) # initialize the error   
Tol = 10^-5
while error > Tol:
           n2 += 1
           X_result = X_upper - ((F(X_upper)*(X_lower-X_upper))/(F(X_lower)-F(X_upper)))
           F_result = F(X_result)
           
           if( F_result == 0 ):        
               print('Got lucky! root =',X_result,' F(r)=',F_result)
               print(' in',n2,' tries',' error <=',error/2)             
               break
           elif( F_lower2*F_result < 0 ):
               X_upper = X_result
               F_upper2 = F_result
               
           else:
               X_lower = X_result
               F_lower2 = F_result
           
           error2 = error2/2 # or: = b-a
           if error2 == 0:
               break
           
print("\nFalse Position Iteration: ", n2)
print("False Position Estimate: ",X_result)
           




# NumericalAnalysis_BracketingMethods Description
Demonstrates 3 different Bracketing Methods
1. Graphical
2. Bisection Method
3. False Postion

# Objective
Provide examples and descriptions for anyone learning about Bracketing Methods

# Explanation
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

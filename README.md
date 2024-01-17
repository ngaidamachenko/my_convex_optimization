# Welcome to My Convex Optimization
***

## Task
The goal is to implement own optimization algorithm, using:
- Bisection Method
- Gradient Descent 
- Simplex Method

## Description
For bisection method:
    First, plotted f(x) = (x - 1)^4 + x^2 which can be written as f = lambda x : (x - 1)**4 + x**2
    Second, wrote a simple dichotomous algorithm (bisection method) to find the zero of a function:
        def find_root(f, a, b)
    Third, used find_root to find root of f prime f' = 4*(x - 1)^3 + 2x which can be written as f_prime = lambda x: 4 * (x - 1)**3 + 2

For gradient descent:
    
    Gradient descent. It measures the local gradient of the cost function and goes towards the direction of the descending gradient. Once the gradient cancels out, it means we reached a minimum.

        xk + 1 = xk - α ∇f(xk)

    where ∇f is the gradient of f and α is called the learning rate. This is how big you step towards the direction of the descending gradient.
    In our one dimension example, the gradient of f is simply the derivative of f.

    First step was to write a simple gradient descent function which finds the minimum of a function f:
        def gradient_descent(f, f_prime, start, learning_rate=0.1, precision=0.001, max_iter=1000) 
        where iteration is limited to 1000 prevent infinite loop
        xk + 1 = xk - α ∇f(xk) can be rewritten as x = x - learning_rate * f_prime(x) where gradient = f_prime(x)
    
    The Brent method is used to double check the result, which shows same answer: 0.41

For simplex method:
    Goal was to maximize z = x + 2y
    subject to
        • 2x + y ≤ 10
        • -4x + 5y ≤ 8
        • x - 2y ≤ 3
        • x, y ≥ 0

    Which can be rewritten as:

    maximize z = cT·x
    subject to
        • Ax ≤ b
        • x ≥ 0

    z is called the objective function, A a coefficients matrix, and b the non-negative constraints. The space defined by the constraints equations is called the feasible region.
    This is a convex polytope. It can be shown that so solutions which maximizes the objective function are located on the vertices of this polytope.

    First, numpy arrays for A, b and c were initialized:
        A = np.array([[2,1],[-4,5],[1,-2]]) where matrix [x,y] of each function f(x) 10 = 2x + y | f(y) 8 = -4x + 5y | f(z) 3 = x - 2y
        b = np.array([10,8,3]) where vectors are function values
        c = np.array([-1,-2]) vector coefficients
    Second, using scikit library and its linprog module a function was create that would take in c, A, b and solve the linear problem.
        def solve_linear_problem(A, b, c):
            result = linprog(c, A_ub=A, b_ub=b, method='highs')
        As simplex is depreciated, 'highs' was used instead.
    Using the function optimal value and optimal arguments were found.


## Installation
Clone the repository and run the provided ipython scripts. Ensure you have the necessary dependencies installed.
Libraries used: 

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar, linprog

## Usage
Run cells in Jupyter respective cells in Jupyter notebooks.

### The Core Team
Project completed by Nikita Gaidamachenko

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>

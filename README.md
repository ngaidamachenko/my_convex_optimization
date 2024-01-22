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

maximize   z = cT·x
subject to
      • Ax ≤ b
      • x ≥ 0

z is called the objective function, A a coefficients matrix, and b the non-negative constraints. The space defined by the constraints equations is called the feasible region.
This is a convex polytope. It can be shown that so solutions which maximizes the objective function are located on the vertices of this polytope.

On the picture, we can visualize the feasible region in beige in the middle. The red line represents the function 2x +y = 10, the white one -4x +5y = 8 and blue one represents
the function x - 2y = 3. The area inside the orange polytope is the intersection between all the constraints inequalities.


## Installation
TODO - How to install your project? npm install? make? make re?

## Usage
TODO - How does it work?
```
./my_project argument1 argument2
```

### The Core Team
Project completed by Nikita Gaidamachenko

<span><i>Made at <a href='https://qwasar.io'>Qwasar SV -- Software Engineering School</a></i></span>
<span><img alt='Qwasar SV -- Software Engineering School's Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px' /></span>

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize_scalar



#plot first function
f = lambda x : (x - 1)**4 + x**2

x = np.linspace(-2, 3, 100)
y = f(x_vals)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='f(x) = (x - 1)^4 + x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Plot of the function f(x)')
plt.grid()
plt.legend()
plt.show()


#dichotomous algorithm (bisection method)

def find_root(f, a, b):
    precision = 0.0001
    while abs(b - a) > precision:
        mid = (a + b) / 2.0
        if abs(f(mid)) < precision:
            return mid
        elif f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return mid
from math import cos, atan
import numpy as np
from scipy.optimize import minimize


def f(x):
    return 0.1 * x[0] * x[1]

def ineq_constraint(x):
    return x[0]**2 + x[1]**2 - (5. + 2.2 * cos(10 * atan(x[0] / x[1])))**2


if __name__ == '__main__':
    con = {'type': 'ineq', 'fun': ineq_constraint}
    x0 = [1, 1]
    res = minimize(f, x0, method='SLSQP', constraints=con)
    print(res)
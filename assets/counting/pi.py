import math
import random
from decimal import Decimal, getcontext
D = Decimal
getcontext().prec = 1020

def leibniz(n):
    s = 0
    for i in range(n):
        s += ((-1)**i) / (2*i + 1.0)

    return s*4

def archimedes(n):
    els = D(2) # edge length squared
    sides = 2

    for i in range(n):
        els = D(2) - D(2) * (D(1) - els / D(4)).sqrt()
        sides *= 2

    return D(sides) * els.sqrt()

"""
 Imagine throwing n darts to (r/2)*(r/2) square which is has circle with radius r
 inside. Square area is 4*r^2, circle area is pi*r^2. Ratio of this areas * 4 = pi
"""
def monte_carlo(n):
    inside_circle = 0
    for _ in range(0, n):
        r1 = random.random()
        r2 = random.random()
        if (r1*r1 + r2*r2) < 1:
            inside_circle += 1

    return 4.0 * inside_circle / n

def error(x):
    return abs(D(x) - D(math.pi))

def str_frm(x):
    return "{0:.10f}".format(x)

def evaluate_iterations(i):
    l = leibniz(i)
    a = archimedes(i)
    mc = monte_carlo(i)
    print(i,
        str_frm(l), str_frm(error(l)),
        str_frm(a), str_frm(error(a)),
        str_frm(mc), str_frm(error(mc)),
        sep=';')

def test():
    # Colums: (leibniz, leibniz error), (archimedes, archimedes error), ...
    # Lines: i, values for i iterations
    for i in range(8, 20, 4):
        evaluate_iterations(i)

    for i in range(20, 1021, 100):
        evaluate_iterations(i)

    for i in range(2000, 102001, 10000):
        l = leibniz(i)
        mc = monte_carlo(i)
        print(i,
            str_frm(l), str_frm(error(l)),
            '-;-',
            str_frm(mc), str_frm(error(mc)),
            sep=';')

test()


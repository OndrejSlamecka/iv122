# Only for comparison
import math
from numpy import linspace

# power1: Using square root

def power_intexp(base, exp):
    """
    @type base: rational number
    @type  exp: integer
    """
    b = base
    r = 1
    e = abs(exp)
    while e > 0:
        if e % 2 == 1:
            r *= b
        b *= b
        e = e//2

    if exp < 0:
        r = 1 / r

    return r

def mroot(base, rt):
    l = 0
    r = base
    while r - l > 0.00001:
        mid = (l + r) / 2
        if power_intexp(mid, rt) < base:
            l = mid
        else:
            r = mid

    return l

def power_root(base, exp):
    r = mroot(power_intexp(base, abs(exp*20)), 20)
    if exp < 0:
        r = 1/r

    return r

#################################################

def ln(x):
    if x == 0:
        return None

    s = 0
    if abs(x - 1) <= 1:
        sign = -1
        p = x-1
        for i in range(1, 1000):
            sign *= -1
            s += sign / i * p
            p *= x-1
    else:
        p = 1
        for i in range(1, 1000):
            p *= (x-1)/x
            s += 1/i * p

    return s

def e_to(x):
    r = 1
    f = 1
    p = x
    for i in range(1, 100):
        r += p/f
        f *= (i+1)
        p *= x

    return r


def power_taylor(base, exp):
    """
    Use power_intexp when exponent is integer.
    """
    r = e_to(abs(exp) * ln(base))
    if exp < 0:
        r = 1/r
    return r


#################################################

def test():
    print(power_root(8.8, 6.2), 8.8**6.2)

    s = 0
    for i in linspace(1, 5.0, num=10):
        for j in linspace(1, 5.0, num=10):
            s += abs(power_root(i, j) - i**j)
    print('Average error of power using root: ' + str(s/(10**2)))

test()

"""
print(2.5**2.2)
print(power1(2.5, 2))
print(ln(2.72**5))
print(2.72**5)
print(e_to(5))
print(power2(-2,1/2))
print(ln(1.5))
"""

# Only for comparison
import math
from numpy import linspace
from decimal import Decimal, getcontext
getcontext().prec = 100
D = Decimal

# power1: Using square root

def power_intexp(base, exp):
    """
    @type base: rational number
    @type  exp: integer
    """
    b = D(base)
    r = D(1)
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
    l = 1
    r = base/rt
    while r - l > 0.001:
        mid = (l + r) / 2
        if power_intexp(mid, rt) < base:
            l = mid
        else:
            r = mid

    return l

def power_root(base, exp):
    r = mroot(power_intexp(base, abs(exp*4)), 4)
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
        for i in range(1, 10000):
            sign *= -1
            s += sign / i * p
            p *= x-1
    else:
        p = 1
        for i in range(1, 10000):
            p *= (x-1)/x
            s += 1/i * p

    return s

def e_to(x):
    r = D(1)
    f = D(1)
    p = D(x)
    for i in range(1, 10000):
        r += p/f
        f *= D(i+1)
        p *= D(x)

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

def fmt(x):
    return '{0:.10f}'.format(x)

def run_test(start, end, items):
    r, t = D(0), 0
    for i in linspace(start, end, num=items):
        for j in linspace(start, end, num=items):
            exp = D(i**j)
            r += abs(power_root(i, j) - exp)
            t += abs(power_taylor(i, j) - exp)
    print('Average error on [' + str(start) + ',' + str(end) + ']:')
    print("\tUsing root: " + fmt(r/(items**2)))
    print("\tTaylor series: " + fmt(t/(items**2)))

def test():
    run_test(1,5,10)
    run_test(10,20,10)

test()


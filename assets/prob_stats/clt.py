#!/usr/bin/env python3

from random import randint
import matplotlib.pyplot as plt

k = 6  # Number of sides of our dice

def hist(samples, name):
    plt.figure()
    plt.hist(samples, bins=24)
    plt.savefig(name + '.svg')

def k_a():
    """
    Emulates K_a die roll with probability density function
    f(x) = 6*x for x in {0,1,..,6} and f(x) = 0 otherwise
    """

    # We emulate choosing a point on a line with intervals
    t = randint(1, k*(k+1)//2)

    r = 1
    for i in range(1, k + 1):
        if t <= r: return i
        r += i + 1

def k_b(): return 7 - k_a()

def fifty_fifty():
    if randint(0,1) == 0:
        return k_a()
    else:
        return k_b()


if __name__ == "__main__":
    M = 10000  # Number of the "outer" experiments
    N = 5

    def go(func, name):
        samples = []
        for _ in range(M):
            v = sum([func() for i in range(N)])
            samples.append(v / N)
        hist(samples, name)

    ###

    #go(k_a, 'ka')
    #go(k_b, 'kb')
    #go(fifty_fifty, 'ff')
    #go(fifty_fifty, 'ff')

    # Choose the function for each sample
    samples = []
    for _ in range(M):
        if randint(0,1) == 0:
            func = k_a
        else:
            func = k_b

        v = sum([func() for i in range(N)])
        samples.append(v / N)
    hist(samples, 'per_sample')


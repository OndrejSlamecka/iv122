"""
 This could be optimised by memoizing result (i.e. maximum of a sequence)
 for each number of each sequence. Sequences often share some numbers.
"""

import matplotlib.pyplot as plt

def collatz_max(n):
    m = n # m is max
    while n != 1:
        m = max(m,n)

        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1

    return m

interval = range(1,1000)
values = list(map(collatz_max, interval))

plt.yscale('log')
plt.plot(interval, values, 'ko')
plt.savefig('collatz_max.png')


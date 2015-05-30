#!/usr/bin/env python3

from random import randint
import sys

def chisq_s(expected, observed):
    """
    One value of the sum -- http://www.stat.yale.edu/Courses/1997-98/101/chigf.htm
    """
    return ((observed - expected) ** 2) / expected


if len(sys.argv) != 2:
    print('Pass the number k in the name of the dataset <random[k].txt> ' \
          'in the first argument', file=sys.stderr)
    sys.exit(1)

# Read input
k = sys.argv[1]
file = open("random" + k + ".txt")
line = file.readline()
numbers = list(map(int, line.split()))

def freq(numbers):
    # Calculate expected frequency
    expected = len(numbers) / 6

    # Count frequencies
    freq = [0 for _ in range(7)]
    p = 0
    for n in numbers:
        freq[n] += 1

    # Transform into set of triplets (die roll, frequency, chisq(expected, frequency))
    freq = freq[1:7]
    s = []
    for i, f in enumerate(freq):
        s.append((i+1, f, chisq_s(expected, f)))

    # Print
    for val in s:
        print('{}\t{}\t{:.4f}'.format(*val))

    print('--------'*3)
    chisq = sum(map(lambda v: v[2], s))
    print('\tchi^2:\t{:.4f}'.format(chisq))

def is_palindrom(numbers):
    s = []
    for i in range(len(numbers) // 2):
        s.append(numbers[i])

    for i in range(len(numbers) // 2, len(numbers)):
        n = s.pop()
        if numbers[i] != n:
            return False

    return True


def pattern_freq(l, pattern):
    freq = 0
    p = l.find(pattern, 0)
    while True:
        freq += 1
        p = l.find(pattern, p + len(pattern))
        if p == -1:
            break

    return freq


def pattern_finder(line):
    line = line[:]
    line = line.replace(' ', '')

    # Coefficient for slight benevolence in pattern repetition
    coef = 1.05

    max_pat = ''
    max_pat_freq = 0

    for s in range(0,100):  # String starting at s-th character
        for l in range(6,len(line) // 2 + 1):  # Of length l
            pat = line[s:s+l]
            pat_freq = pattern_freq(line, pat)

            # Pattern frequency should match its length
            if (pat_freq > max_pat_freq and pat_freq > len(line) / (len(pat) * coef)) \
                or (pat_freq == max_pat_freq and len(pat) > len(max_pat)):
                max_pat_freq = pat_freq
                max_pat = pat

    return (max_pat, max_pat_freq)

freq(numbers)
print('Is a palindrom:', is_palindrom(numbers))

pat_r = pattern_finder(line)
print('Pattern repetition: {}, length = {}, frequency = {}'.format(pat_r[0],
                                                    len(pat_r[0]), pat_r[1]))

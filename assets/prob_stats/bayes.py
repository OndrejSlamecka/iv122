#!/usr/bin/env python3

from random import randint
from operator import mul
from functools import reduce

### Dice

def die_1(v): return 1/6

def die_2(v):
    # 2 is not present, instead 5 is present twice as much
    if v == 5:
        return 2/6
    else:
        return 1/6

def die_3(v):
    if v == 6:
        return 2/7
    else:
        return 1/7

### Bayes

def P(sequence, H):
    """
    Returns P(D|H) -- the probability of this sequence occuring
    with hypothesis H
    """
    return reduce(mul, map(H, sequence), 1)


def bayes(hypotheses, h, seq):
    """
    P(h|seq) = P(seq|h)*P(h) / P(seq)
    """
    p_seq = sum(map(lambda d: P(seq, d[0]) * d[1], hypotheses))
    return P(seq, hypotheses[h][0]) * hypotheses[h][1] / p_seq

### Main

def explore(name, hypotheses, seq):
    print('Hypotheses distribution ' + name)
    for i in range(len(hypotheses)):
        print('P(H_' + str(i+1) + '|seq) = ', end='')
        print(bayes(hypotheses, i, seq))
    print('')

if __name__ == "__main__":
    seq = [1, 3, 4, 5, 1, 4, 6, 5, 1, 5, 4, 5]

    """
    By hypotheses we understand a list where each item is a pair (f,p),
    such that (f,p) is a hypothesis with function f giving probability
    for each die roll in this hypothesis and with probability p of this
    hypothesis occuring
    """
    problem = {'uniform': [(die_1, 1/3), (die_2, 1/3), (die_3, 1/3)],
               'pref_d3': [(die_1, 5/100), (die_2, 5/100), (die_3, 90/100)]}

    for name in problem:
        explore(name, problem[name], seq)

# Pythonic approach would use yield

def perm(l):
    if len(l) == 1: return [l]

    r = []
    for i in range(len(l)):
        for p in perm(l[:i] + l[i + 1:]):
            r.append([l[i]] + p)

    return r

def comb(l, k, repetitions = False):
    if k == 0 or len(l) == 0: return [[]]
    r = []

    nl = l[:]
    if not repetitions:
        nl = l[1:]

    for c in comb(nl, k-1, repetitions):
        if len(c) >= k-1:
            r.append([l[0]] + c)

    for c in comb(l[1:], k, repetitions):
        if len(c) > 0:
            r.append(c)

    return r

def var(l, k, repetitions = False):
    if k == 0: return [[]]

    r = []
    for i in l:
        nl = l[:]
        if not repetitions:
            nl.remove(i)

        for v in var(nl, k-1, repetitions):
            r.append([i] + v)

    return r

####

def test():
    p = perm([1,2,3])
    print('Permutations of [1,2,3] (' + str(len(p)) + ' total): ', p)

    c1 = comb([1,2,3], 2, False)
    print("2-sets of [1,2,3] (combinations without repetition, " + \
            str(len(c1)) + " total):\n\t", c1)
    c2 = comb([1,2,3], 2, True)
    print("2-multisets of [1,2,3] (combinations with repetition, " + \
            str(len(c2)) + " total):\n\t", c2)

    v1 = var([1,2,3], 2, False)
    print("2-tuples of [1,2,3] without repetition (variations, " + \
            str(len(v1)) + " total):\n\t", v1)
    v2 = var([1,2,3], 2, True)
    print("2-tuples of [1,2,3] with repetition (variations, " + \
            str(len(v2)) + " total):\n\t", v2)

test()

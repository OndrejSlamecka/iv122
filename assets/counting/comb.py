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


#print(perm([1,2,3]))
#print(len(perm([1,2,3,4])) == 24)
#print(len(comb([1,2,3,4], 3)) == 4)
#print(comb([1,2,3,4], 2))
#print('~~')
print(comb([1,2,3,4], 2, True))
print(comb([1,2,3,4], 2, False))

#print(var([1,2,3,4], 2, True))
#print(var([1,2,3,4], 2, False))

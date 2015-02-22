# Pythonic approach would use yield

def perm(l):
    r = []
    if len(l) == 1:
        return [l]
    
    for i in range(len(l)):
        for p in perm(l[:i] + l[i + 1:]):
            r.append([l[i]] + p)

    return r

def var_r(l, k):
    r = []
    if k == 0:
        return [[]]
        
    for i in range(len(l)):
        for v in var_r(l, k-1):
            r.append([l[i]] + v)

    return r


print(perm([1,2,3]))
print(len(perm([1,2,3,4])) == 24)

print(var_r([0,1,2],3))

import math


def nCr(n,r):
     if n-r<0: return 0
     f = math.factorial
     return f(n) / f(r) / f(n-r)

def swap(list):
    d = dict()
    counter = dict()
    for elt in list:
        if elt in d: d[elt]+=1
        else:
            d[elt]=1
    #for k,v in d.iteritems():
    #    if v in counter: counter[v]+=1
    #    else:
    #        counter[v]=1
    result = nCr(len(list), 2)
    # for k,v in counter.iteritems():
    #    if k!=1: result -= v*nCr(k, 2)
    for k,v in d.iteritems():
        if v!=1: result -= nCr(v, 2)
    if (len(set(list)) != len(list)): result += 1
    return result 

list =    [4, 7, 4]
print swap(list)
list =    [1, 47]
print swap(list)
list=    [9, 9, 8,8]
print swap(list)

list = [22, 16, 36, 35, 14, 9, 33, 6, 28, 12, 18, 14, 47, 46, 29, 22, 14, 17, 4, 15, 28, 6, 39, 24, 47, 37]
print swap(list)

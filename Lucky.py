def check(wynik):
    i = 0
    while (i<len(wynik)-1):
        if wynik[i] == wynik[i+1]: return False
        i+=1
    return True

sum = 0
def perm(list, wynik, N):
    if N==len(wynik): 
        global sum
        if check(wynik): sum+=1
        return 
    for index, elt in enumerate(list):
        wynik.append(elt)     
        list.pop(index)      
        perm(list, wynik, N)
        list.insert(index, elt)  
        wynik.pop()      


def factorial(n):return reduce(lambda x,y:x*y,[1]+range(1,n+1))

l=[1,2,3,4,5]
#l=list("abbaa")
l=list("ab")
#l=list("aaab")
#l=list("abcdefghij")

d = dict()
for elt in l:
    if not elt in d:
        d[elt]=1
    else:
        d[elt]+=1
perm(l, [], len(l))
for k,v in d.iteritems():
    sum/=factorial(v)
print sum




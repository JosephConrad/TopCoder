
def subset(l, s, index):
    print s
    for i in range(index,len(l)):
        s.append(l[i])
        subset(l, s, i+1)
        s.pop()

l = [1,2,3,5]

subset(l, [], 0)

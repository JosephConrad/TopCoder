
tab = [1,1]
for i in range(2,61):
    tab.append(tab[i-1]-1+2*tab[i-2]+1)
print tab

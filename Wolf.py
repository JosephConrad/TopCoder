
pat='wolf'

def remDup(word):
    i=len(word)-1
    while i!=0:
        if word[i]==word[i-1]: word.pop(i-1)
        i-=1
    return word

def wolf(word):
    i=0
    while i<len(word)-1:
        if ''.join(word[i:i+4]) != pat: return 'INVALID'
        i+=4
    return 'VALID'


w = list('wwolfolf')
w = list('wolf')
w = list('flowolf')
w = list("wolfwwoollffwwwooolllfffwwwoooollllffff")
print remDup(w)
print wolf(remDup(w))

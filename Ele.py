def elephant(word):
    if len(word) == 0: return 0
    current = '' 
    maks = 0
    maksGlobal = 0
    for elt in word:
        if elt == current:  
            maks += 1
            if maks > maksGlobal: maksGlobal = maks
        else:
           maks = 1
           current = elt
    return len(word)-maksGlobal
        
        
word = "RRGGBB"
print elephant(word)
word = "RGBRGB"
print elephant(word)
word = "R"
print elephant(word)
word = "RGGGBB"
print elephant(word)
word = "RGBRBRGRGRBBBGRBRBRGBGBBBGRGBBBBRGBGRRGGRRRGRBBBBR"
print elephant(word)

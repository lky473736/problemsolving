S = input ()

word_seperating = []

for charnum in range (len(S)) :
    word_seperating.append (S[charnum])

lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
   'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
   
finder = []

for i in range (len(lowercase_alphabet)) :
    if lowercase_alphabet[i] in word_seperating :
        finder.append (word_seperating.index(lowercase_alphabet[i]))
    
    else : 
        finder.append (-1)
        
for k in finder :
    print (k, end = ' ')

def alphabet_finder(k) :
    if k in ['A', 'B', 'C']:
        return 3
        
    elif k in ['D', 'E', 'F']:
        return 4
        
    elif k in ['G', 'H', 'I']:
        return 5
        
    elif k in ['J', 'K', 'L']:
        return 6
        
    elif k in ['M', 'N', 'O']:
        return 7
        
    elif k in ['P', 'Q', 'R', 'S']:
        return 8
        
    elif k in ['T', 'U', 'V']:
        return 9
        
    elif k in ['W', 'X', 'Y', 'Z']:
        return 10

grandma_word = input()

sum = 0
wordlist = []

for i in range (len(grandma_word)) :
    wordlist.append (grandma_word[i])

for j in wordlist :
    sum = sum + alphabet_finder(j)
    
print (sum)

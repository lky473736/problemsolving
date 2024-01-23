'''minsik = ['a', 'b', 'k', 'd', 'e', 'g', 'h', 'i', 
          'l', 'm', 'n', 'ng', 'o', 'p', 'r', 's', 
          't', 'u', 'w', 'y']'''
          
import sys
          
minsik = {'a': 0, 'b': 1, 'k': 2, 'd': 3, 'e': 4, 'g': 5, 'h': 6, 'i': 7, 'l': 8, 'm': 9, 'n': 10, 'ng': 11, 'o': 12, 'p': 13, 'r': 14, 's': 15, 't': 16, 'u': 17, 'w': 18, 'y': 19}

def minsik_sort(word) :
    return [minsik[c] for c in word]
          
N = int(input())

wordlist = []

for _ in range (N) :
    str_input = sys.stdin.readline().rstrip()
    len_str_input = len(str_input)

    alphabet = []
    
    i = 0
    
    while i < len_str_input :
        if i < len_str_input - 1 :
            if str_input[i] == "n" and str_input[i+1] == "g" :
                alphabet.append("ng")
                i += 2
            
            else :
                alphabet.append (str_input[i])
                i += 1
                
        else :
            alphabet.append (str_input[i])
            i += 1
            
    wordlist.append (alphabet)
    
wordlist = sorted(wordlist, key=minsik_sort)

for word in wordlist :
    print ("".join(word))
T = int(input())

wordlist = []
for i in range (T) :
    word = input()
    wordlist.append(word)
    
for j in wordlist :
    print (j[0] + j[-1])

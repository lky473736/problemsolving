alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numlist = [0 for i in range (len(alphabet_list))]

N = int(input())

for j in range (N) :
    name = input()
    
    indexing = alphabet_list.index(name[0])
    
    numlist[indexing] += 1

count = 0

for k in range(len(numlist)) : 
    if numlist[k] >= 5 :
        print (alphabet_list[k], end = "")
        count += 1

if count == 0 :
    print ("PREDAJA")
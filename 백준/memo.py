N, M = map(int, input().split())
square = []

def findindex(num, arr) :
    slist = []
    for i in range (len(arr)) :
        if num == arr[i] :
            slist.append (i)
            
    return slist

finder = []
for i in range (N) : 
    compo = input()
    finder.append ([])
    for x in range (len(compo)) :
        finder[-1].append (int(compo[x]))
    
print (finder)
    
for j in range (N) : # for j in finder
    for num in finder[j] :
        if finder[j].count(num) >= 2 : # >=
            indexlist = findindex(num, finder[j])
            print (indexlist)

            for k in range (j + 1, N) :
                if finder[k].count(num) == 2 : # >=
                    guess = findindex(num, finder[k])
                    print (guess)
                    
                    for p in range (len(indexlist)) : # 이웃하지 않아도 체크해야 함 
                        if p == len(indexlist) - 1:
                            compo_il = indexlist[-1] - indexlist[0]
                        else:
                            compo_il = indexlist[p+1] - indexlist[p]
                        
                        for q in range(len(guess)):
                            if q == len(indexlist) - 1:
                                compo_gu = guess[-1] - guess[0]
                            else:
                                compo_gu = guess[q+1] - guess[q]

                                if (k - j == compo_il and compo_il == compo_gu) :
                                    square.append ((k - j + 1) ** 2)

print (square)

if square == [] :
    print (1)
    
else :
    print (max(square))

N = int(input())
card = [i+1 for i in range(N)]
trs = []

if N == 1 :
    print (1)
    exit()

while len(card) != 1 : 
    trs.append (card[0])
    card.pop(0)
    card.append (card[0])
    card.pop(0)
    
for i in trs :
    print (i, end = ' ')
    
    if i == trs[-1] : 
        print (card[0])
        
        
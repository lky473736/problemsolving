import sys

N = int(sys.stdin.readline())
slist = list(map(int, sys.stdin.readline().split()))

slist = sorted(slist)
# sdict = dict()

# for compo in slist : 
#     sdict[compo] = 0


page = 0

while True : 
    # print (slist)
    
    if N == 0 :
        break
    
    else :
        page += 1
        temp = slist[-1]
        # print (temp)
        
        for compo in slist[::-1] : 
            if temp // compo < 2 :
                N -= 1
                slist.pop()
            
print (page)
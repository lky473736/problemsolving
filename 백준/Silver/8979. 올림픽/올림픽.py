import sys

N, K = map(int, sys.stdin.readline().split())

country = []

for _ in range (N) : 
    country.append(list(map(int, sys.stdin.readline().split())))
    
country.sort(key = lambda x : (x[0]))

gold = [[country[i][0], country[i][1]] for i in range (N)]
silver = [[country[i][0], country[i][2]] for i in range (N)]
bronze = [[country[i][0], country[i][3]] for i in range (N)]

gold.sort(key = lambda x : (-x[1]))

'''
silver.sort(key = lambda x : (x[0]))
bronze.sort(key = lambda x : (x[0]))
'''

rank = [[0, gold[i][0]] for i in range (N)] # 순위, 현재 성분
rank[0][0] = 1 

counting = 1

for i in range (1, N) :
    if gold[i-1][1] == gold[i][1] :
        if silver[gold[i-1][0] - 1][1] > silver[gold[i][0] - 1][1] :
            counting += 1
            rank[i][0] = counting
            pass
        
        elif silver[gold[i-1][0] - 1][1] < silver[gold[i][0] - 1][1] : 
            rank[i-1], rank[i] = rank[i], rank[i-1]
            rank[i][0] += 1
            rank[i-1][0] = rank[i][0] - 1
            
        else : 
            if bronze[gold[i-1][0] - 1][1] > bronze[gold[i][0] - 1][1] :
                counting += 1
                rank[i][0] = counting
                pass
            
            elif bronze[gold[i-1][0] - 1][1] < bronze[gold[i][0] - 1][1] : 
                rank[i-1], rank[i] = rank[i], rank[i-1]
                rank[i][0] += 1
                rank[i-1][0] = rank[i][0] - 1
                
            else : 
                rank[i][0] = rank[i-1][0]
                pass
            
    else :
        counting += 1 
        rank[i][0] = counting 
        
    if rank[i] == K : 
        break
    
rank.sort(key = lambda x : (x[1]))
    
for i in range (N) :
    if rank[i][1] == K : 
        break
    
print (rank[i][0])
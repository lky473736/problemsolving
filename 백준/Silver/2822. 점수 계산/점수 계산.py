import sys

numlist = []

for i in range (8) : 
    num = int(sys.stdin.readline())
    numlist.append([i+1, num])
    
numlist.sort(key = lambda x : -x[1])

rst = numlist[:5]
print (sum([rst[i][1] for i in range(5)]))

for i in sorted([rst[k][0] for k in range(5)]) :
    print (i, end = ' ')
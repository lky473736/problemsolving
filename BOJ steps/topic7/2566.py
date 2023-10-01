'''
출강 끝나고 해결하기 

matrix = []
finder = []

for i in range (9) :
    row = list(map(int, input().split()))
    matrix.append (row)
    
    finder_component = [max(row), i, row.index(max(row))]
    finder.append (finder_component)

for j in range (len(finder)) :
    if finder[j][0] >= finder[j - 1][0] :
        output = finder[j]
    
    print (output)
        
print (output[0])
print (output[1], output[2])''' 

matrix = []
finder = []
for_finder = []
output = 0

for i in range (9) :
    row = list(map(int, input().split()))
    matrix.append (row)
    
    finder_component = [max(row), i + 1, row.index(max(row)) + 1]
    finder.append (finder_component)
    
for k in range (len(finder)) :
    for_finder.append (finder[k][0])
    
maxium_index = for_finder.index(max(for_finder))

output = finder[maxium_index]
        
print (output[0])
print (output[1], output[2])

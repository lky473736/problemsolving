N, M = map(int, input().split())

list_input = []

for i in range (M) :
    compo = list(input().split())
    compo[0] = int(compo[0])
    compo[1] = int(compo[1])
    list_input.append(compo)
    
list_input.sort(key = lambda x : [x[1], x[0]])

for i in list_input :
    print (i[2], end='')
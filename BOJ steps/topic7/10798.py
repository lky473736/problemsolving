# sibal yeongseok...

'''
wlist = []
lenlist = []

for i in range (5) :
    component = input().split()
    wlist.append (component)
    
print (wlist)

for m in range (5) :
    lenlist.append(len(wlist[m][0]))
    
max_lenindex = lenlist.index(max(lenlist))
print (max_lenindex)

for n in range (5) :
    if max_lenindex > len(wlist[n][0]) :
        wlist[n][0] = wlist[n][0] + '_' * (max_lenindex - len(wlist[n][0]))

for j in range (max_lenindex) :
    for k in range (5) :
        print (wlist[k][0][j], end = '')
'''

wlist = []
lenlist = []

for i in range(5):
    component = input().split()
    wlist.append(component)
    
for m in range(5):
    lenlist.append(len(wlist[m][0]))

max_len = max(lenlist)

for n in range(5):
    if max_len > len(wlist[n][0]):
        wlist[n][0] = wlist[n][0] + '_' * (max_len - len(wlist[n][0]))

for j in range(max_len):
    for k in range(5):
        if wlist[k][0][j] != '_' :
            print(wlist[k][0][j], end='')
            
        else :
            pass
        

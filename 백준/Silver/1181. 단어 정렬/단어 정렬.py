'''alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def comparedict_returnsm(a, b):
    for i in range(len(a)):
        if alphabet.index(a[i]) == alphabet.index(b[i]):
            pass
        else:
            if alphabet.index(a[i]) > alphabet.index(b[i]):
                return b
            else:
                return a

slist = []

N = int(input())

for i in range(N):
    compo = input()
    
    if compo in slist : 
        pass
    else :
        slist.append (compo)

slist = sorted(slist, key = lambda x : len(x))

print (slist)

finder = []

for j in range(len(slist) - 1):
    if slist[j][1] == slist[j + 1][1]:
        print(comparedict_returnsm(slist[j][0], slist[j + 1][0]))
    else:
        print(slist[j][0])
print(slist[-1][0])  # 마지막 요소 출력
'''

N = int(input())
slist = []

for i in range(N):
    compo = input()
    
    if compo in slist : 
        pass
    else :
        slist.append (compo)
        
slist = sorted (slist) # 사전식 정렬
slist = sorted(slist, key = lambda x : len(x)) # 길이순 정렬
for i in slist : print (i)
import sys

N = int(sys.stdin.readline())
listn = map(int, sys.stdin.readline().split())

dicti = dict()

for compo in listn :
    try :
        dicti[compo] += 1
        
    except KeyError :
        dicti[compo] = 1

M = int(sys.stdin.readline())
listm = map(int, sys.stdin.readline().split())

for compo in listm :
    try :
        print (dicti[compo], end=' ')
        
    except :
        print (0, end=' ')
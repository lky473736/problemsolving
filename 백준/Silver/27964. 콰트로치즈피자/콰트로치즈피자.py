import sys

N = int(sys.stdin.readline())
toping = list(map(str, sys.stdin.readline().rstrip().split()))

cheese = set()
cnt = 0

for top in toping :
    if top[-6:] == "Cheese" :
        if top not in cheese :
            cheese.add(top)
            cnt += 1

if cnt >= 4 :
    print ("yummy")
    
else :
    print ("sad")
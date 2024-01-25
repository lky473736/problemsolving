import sys

N = int(sys.stdin.readline())

position = list(map(int, sys.stdin.readline().split()))

sorted_position = list(sorted(set(position)))
sorted_position = {sorted_position[i] : i for i in range (len(sorted_position))}

for i in position : 
    print (sorted_position[i], end = ' ')

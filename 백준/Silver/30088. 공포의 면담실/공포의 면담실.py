import sys

N = int(sys.stdin.readline())
working_time = []

for i in range (N) :
    lst = list(map(int, sys.stdin.readline().split()))
    num_worker = lst[0]
    worker = lst[1:]
    
    working_time.append (sum(worker))

working_time.sort()

suma = 0

# print (working_time)

for i in range (N) : 
    suma += sum(working_time[:i+1])
    
print (suma)
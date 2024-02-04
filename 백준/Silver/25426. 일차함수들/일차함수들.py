import sys

N = int(sys.stdin.readline())
lst_param = list()

for _ in range (N) :
    a, b = map(int, sys.stdin.readline().split())
    lst_param.append ([a, b])

suma = 0
lst_param.sort()

for i in range (N) : 
    suma += lst_param[i][0] * (i+1) + lst_param[i][1]

print (suma)
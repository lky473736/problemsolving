N = int(input())

time = list(map(int, input().split()))

finder = sorted(time)

suma = 0
k = 0

for i in finder : 
    k += i
    suma += k

print (suma)
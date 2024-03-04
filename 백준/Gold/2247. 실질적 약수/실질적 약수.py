# https://cobokjang.tistory.com/14

A = int(input())

P = 0

for i in range(2, int(A/2 + 1)) :
    P += i*(A//i -1) % 1000000

print (P % 1000000)
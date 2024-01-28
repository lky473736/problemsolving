'''
5 3
99291
//answer : 99

6 3
773671
//answer : 777

4 2
9879
//answer : 99

10 3
2222211113

//answer : 2222213

10 3

1111122223

//answer : 1122223
'''

import sys

N, K = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline().rstrip())
num = [int(i) for i in num]
stack = []

i = 0
length = 0

if sorted(num, reverse=True) == num : 
    for i in num[:N-K] : 
        print (i, end = "")
        
    exit()

while True : 
    if K == 0 or i >= N :
        break
        
    while K > 0 and stack != [] and stack[-1] < num[i] : 
        stack.pop()
        length += 1
        K -= 1
    
    stack.append (num[i])
    length += 1
    i += 1

if i < N :
    for j in num[i:] : 
        stack.append (j)

while K > 0 :
    stack.pop()
    K -= 1
    
for i in stack : 
    print (i, end = "")
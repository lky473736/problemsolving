'''
# nested loopstations is baddest in this situation!

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

for i in range (N-1) : 
    key = 0
    for j in range (i+1, N) : 
        if A[i] < A[j] : 
            key = 1
            break
    
    if key == 0 :
        print (-1)
        
    else :    
        print (A[j])
    
print (-1)
'''

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A = [[A[i], i] for i in range (N)]

stack = []
num_stack = 0
rst = [-1] * N

for i in range (1, N) :
    if A[i-1][0] < A[i][0] : 
        rst[i-1] = A[i][0]
        
        '''if stack != [] : # stack에 뭔가가 있다면
            cls_num_stack = 0
            
            for j in range (num_stack) : 
                if stack[j][0] < A[i][0] and stack[j] != [-1, -1] : # [-1, -1] == the key of escape
                    rst[stack[j][1]] = A[i][0]
                    stack[j] = [-1, -1]
                    cls_num_stack += 1
                    
            num_stack -= cls_num_stack'''
            
        '''if stack != [] : # stack에 뭔가가 있다면
            j = 0
            while j < num_stack : 
                print (stack)
                if stack[-1-j][0] < A[i][0] : 
                    rst[stack[-1-j][1]] = A[i][0]
                    stack.pop()
                    num_stack -= 1
                j += 1'''
                
        while stack and stack[-1][0] < A[i][0]:
            rst[stack[-1][1]] = A[i][0]
            stack.pop()
                    
    else :
        stack.append(A[i-1])
        
print (*rst)
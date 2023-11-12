# queue

import sys
input = sys.stdin.readline().rstrip()
N = int(input)

slist = []

def push(X) : 
    slist.append (X)
    
def pop() :
    if slist == [] :
        print (-1)
        
    else :
        print (slist[0])
        slist.pop(0)
        
def size() :
    print (len(slist))
    
def empty() :
    if slist == [] :
        print (1)
        
    else :
        print (0)
        
def front() :
    if slist == [] :
        print (-1)
        
    else :
        print (slist[0])

def back() :
    if slist == [] :
        print (-1)
        
    else :
        print (slist[-1])

for i in range (N) :
    input = sys.stdin.readline().rstrip()
    
    if 'push' in input : 
        push(input.split(' ')[1])
        
    elif input == 'pop' :
        pop()
        
    elif input == 'size' :
        size()
        
    elif input == 'empty' : 
        empty()
        
    elif input == 'front' :
        front()
        
    elif input == 'back' : 
        back()
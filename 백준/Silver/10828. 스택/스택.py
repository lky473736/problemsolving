# FIFO
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
        print (slist[-1])
        slist.pop()
        
def size() :
    print (len(slist))
    
def empty() :
    if slist == [] :
        print (1)
        
    else :
        print (0)
        
def top() :
    if slist == [] :
        print (-1)
        
    else :
        print (slist[-1])
        
for i in range (N) :
    input = sys.stdin.readline().rstrip()
    command = input
    
    if 'push' in command :
        push(command.split (' ')[1])
        
    elif command == 'pop' :
        pop()
        
    elif command == 'size' :
        size()
        
    elif command == 'empty' : 
        empty()
        
    elif command == 'top' :
        top()

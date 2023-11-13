import sys
input = sys.stdin.readline().rstrip()

N = int(input)

deque = []

def push_front(X) :
    global deque
    deque = deque[::-1]
    deque.append (X)
    deque = deque[::-1]
    
def push_back(X) : 
    deque.append (X)
    
def pop_front() : 
    if deque == [] :
        print (-1)
    
    else :    
        print (deque[0])
        deque.pop(0)
        
def pop_back() :
    if deque == [] :
        print (-1)
    
    else :    
        print (deque[-1])
        deque.pop(-1)
        
def size() :
    print (len(deque))
    
def empty() :
    if deque == [] :
        print (1)
    
    else :    
        print (0)
        
def front() :
    if deque == [] :
        print (-1)
    
    else :    
        print (deque[0])
        
def back() :
    if deque == [] :
        print (-1)
    
    else :    
        print (deque[-1])
        
for i in range (N) :
    input = sys.stdin.readline().rstrip()
    operation = input
    
    if 'push_front' in operation : 
        push_front(int(operation.split(' ')[1]))
        
    elif 'push_back' in operation : 
        push_back(int(operation.split(' ')[1]))
        
    elif operation == 'pop_front' : 
        pop_front()
        
    elif operation == 'pop_back' : 
        pop_back()
        
    elif operation == 'size' : 
        size()
        
    elif operation == 'empty' : 
        empty()
        
    elif operation == 'front' : 
        front()
        
    elif operation == 'back' : 
        back()
        
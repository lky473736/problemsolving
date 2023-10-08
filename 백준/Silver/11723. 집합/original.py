import sys

def add (S, n) :
    if n in S : 
        pass
    
    else :
        S.append(n)
    
def remove (S, n) :
    if n not in S :
        pass
    
    else : 
        S.remove(n)
        
def check (S, n) :
    if n in S : 
        print (1)
        
    else :
        print (0)
        
def toggle (S, n) :
    if n in S : 
        S.remove(n)
        
    else :
        S.append(n)
        
def allf (S, n) :
    S = [i + 1 for i in range (20)]
    
def empty (S, n) :
    S = []
    
'''def system (functionname, S, argument) :
    match functionname :
        case 'add' :
            add (S, argument)
        
        case 'remove' :
            remove (S, argument)
        
        case 'check' :
            check (S, argument)
            
        case 'toggle' :
            toggle (S, argument)
            
        case 'all' :
            allf (S, argument)
        
        case 'empty' :
            empty (S, argument)
    
N = int(input())
S = []

for i in range (N) :
    order = list(input().split())
    
    if len(order) == 2 : 
        system (order[0], S, int(order[1]))
        
    else :
        system (order[0], S, order[0])'''
        
def system(functionname, S, argument):
    if functionname == 'add':
        add(S, argument)
    elif functionname == 'remove':
        remove(S, argument)
    elif functionname == 'check':
        check(S, argument)
    elif functionname == 'toggle':
        toggle(S, argument)
    elif functionname == 'all':
        allf(S, argument)
    elif functionname == 'empty':
        empty(S, argument)

N = int(sys.stdin.readline().strip())
S = []

for i in range(N):
    order = sys.stdin.readline().strip().split()
    
    if len(order) == 2:
        system(order[0], S, int(order[1]))
        
    else:
        system(order[0], S, order[0])

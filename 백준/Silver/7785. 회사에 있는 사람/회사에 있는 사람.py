import sys

n = int(sys.stdin.readline())
person = set()

for _ in range (n) :
    name, log = sys.stdin.readline().split()
    
    if name not in person and log == 'enter' : 
        person.add (name)
        
    else :
        person.remove (name)
        
for compo in sorted(list(person), reverse=True) :
    print (compo)
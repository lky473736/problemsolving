import sys

N = int(sys.stdin.readline())

files = dict()

for i in range (N) :
    _, extension = sys.stdin.readline().rstrip().split(".")
    
    try :
        files[extension] += 1
        
    except : 
        files[extension] = 1
        
items = sorted(list(files.items()), key = lambda x : (x[0]))

for item in items : 
    print (item[0], item[1])
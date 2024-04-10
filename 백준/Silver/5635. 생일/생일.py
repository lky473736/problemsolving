import sys

n = int(sys.stdin.readline())
lst = []

for i in range (n) :
    name, day, month, year = sys.stdin.readline().rstrip().split()
    day = int(day)
    month = int(month)
    year = int(year)
    
    lst.append ([name, day, month, year])
    
lst.sort (key = lambda x : (x[3], x[2], x[1]))

print (lst[-1][0])
print (lst[0][0])
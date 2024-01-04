import sys

N, M = map(int, sys.stdin.readline().split())
db = dict()

for _ in range (N) : 
    site, pw = sys.stdin.readline().rstrip().split()
    db[site] = pw
    
for _ in range (M) :
    target_site = sys.stdin.readline().rstrip()
    print(db[target_site])
import sys

S = sys.stdin.readline().rstrip()

suffix = []

for i in range (len(S)) :
    suffix.append (S[i:])
    
for compo in sorted(suffix) :
    print (compo)
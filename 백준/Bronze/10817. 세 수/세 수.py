numlist = []

A, B, C = map(int, input().split())

numlist.append (A)
numlist.append (B)
numlist.append (C)
numlist.sort()

print (numlist[1])
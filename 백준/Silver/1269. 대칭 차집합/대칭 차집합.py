nA, nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

P = A.union(B) - A.intersection(B)

print (len(P))
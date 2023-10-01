A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

print (str((A+B)%C))
print (str(((A%C) + (B%C))%C))
print (str((A*B)%C))
print (str(((A%C) * (B%C))%C))

N = int(input())

for i in range (N - 1) :
    print (' ' * (N - i - 1) + '*' * (2 * (i + 1) - 1)) # N - ~ ...
    
print ('*' * (2 * N - 1)) # N번째 항

for i in range (N - 1) : # N+1, N+2 ...
    print (' ' * (i + 1) + '*' * (2*N - 2*i - 3))

import sys
import itertools

C = int(sys.stdin.readline()) # testcase

for _ in range (C) : 
    S, N, T, L = map(str, sys.stdin.readline().rstrip().split())
    N = int(N)
    T = int(T)
    L = int(L)
    
    behavior = 100000000
    token = 0
    
    if S == "O(N)" :
        if N * T <= behavior * L :
            token = 1
            
    elif S == "O(N^2)" : 
        if (N**2) * T <= behavior * L : 
            token = 1
        
    elif S == "O(N^3)" : 
        if (N**3) * T <= behavior * L : 
            token = 1
        
    elif S == "O(2^N)" : 
        if (2**N) * T <= behavior * L : 
            token = 1
        
    else :
        fact = 1
        
        while N != 1 :
            fact *= N
            
            if fact * T > behavior * L : 
                break
            
            N -= 1
            
        if fact * T <= behavior * L : 
            token = 1
        
    if token == 1 :
        print ("May Pass.")
        
    else :
        print ("TLE!")
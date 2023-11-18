A, B, N = map(int, input().split())

fshare = A // B
frest = A - 1 * (B * fshare)

for i in range (N) :
    if frest * 10 < B :
        fshare = 0 
        frest = frest * 10
      
    else : 
        fshare = (frest * 10) // B
        frest = frest * 10  - fshare * B

print (fshare)
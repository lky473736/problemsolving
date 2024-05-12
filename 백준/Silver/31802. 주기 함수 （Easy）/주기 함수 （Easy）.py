import sys

p = int(sys.stdin.readline())
sumations = list(map(int, sys.stdin.readline().split()))
positives, negatives = [0], [0]

psuma, nsuma = 0, 0
for i in range (p) :
    psuma = psuma + sumations[i]
    positives.append (psuma)

    nsuma = nsuma + sumations[p-1-i]
    negatives.append (nsuma)

i, j = map(int, sys.stdin.readline().split())

rst = 0

if i == j :
    rst = 0

else :
    psuma = positives
    nsuma = negatives
    
    if i < 0 and j < 0 :
        i, j = abs(i), abs(j)
        alpha = (i // p) * nsuma[-1] + nsuma[i%p]
        beta = (j // p) * nsuma[-1] + nsuma[j%p]
        rst = alpha - beta
        
    elif i < 0 and j == 0 :
        i = abs(i)
        rst = nsuma[i]

    elif i < 0 and j > 0 :
        i = abs(i)
        alpha = (i // p) * nsuma[-1] + nsuma[i%p]
        beta = (j // p) * psuma[-1] + psuma[j%p]
        rst = alpha + beta

    elif i == 0 and j > 0 :
        rst = psuma[j]

    else :
        alpha  = (i // p) * psuma[-1] + psuma[i%p]
        beta = (j // p) * psuma[-1] + psuma[j%p]
        rst = beta - alpha

print (rst)
import sys
import math 
import itertools

def eratosthenes (N) :
    nums = [0 for i in range (N + 1)]
    
    for i in range (2, int(math.sqrt(N) + 1)) : # 0, 1은 소수 아님
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums

prime = eratosthenes(1000000)
prime[0] = 1
nprime = prime.copy()
nprime = [index for index in range(1000000) if nprime[index] == 0]
nprime = set(nprime)

'''n = int(sys.stdin.readline())
copy_n = n

if n < 8 : 
    print (-1)
    exit()

temp = n // 2 # always even num
n = n - temp

rst = [0, 0, 0, 0]

while rst[0] not in nprime or rst[1] not in nprime or rst[2] not in nprime or rst[3] not in nprime :
    if n == 1 or temp > copy_n : 
        print (-1)
        exit()
        
    for i in range (2) :
        l = []
        
        for j in range (2, n) : 
            if j in nprime and n - j in nprime :
                l.append((j, abs(j - (n - j))))
        
        if l != [] : 
            l.sort(key = lambda x : x[1])
            
            rst[i] = l[0][0]
            rst[i+2] = n - l[0][0]

        n = temp
        
    temp += 2
    
    n = copy_n - temp
    
for i in sorted(rst) : 
    print (i, end = ' ')'''
    
N = int(sys.stdin.readline())

if N < 8 :
    print (-1)
    exit()

if N % 2 == 0 :
    rst = [2, 2, 0, 0] # trick of goldbach
    N -= 4
    
else :
    rst = [2, 3, 0, 0]
    N -= 5
    
l = []
    
for j in range (2, N) : 
    if j in nprime and N - j in nprime :
        l.append((j, abs(j - (N - j))))

if l != [] :
    l.sort(key = lambda x : x[1])
    rst[2], rst[3] = l[0][0], N - l[0][0]
    
    for i in rst :
        print (i, end = ' ')

else :
    print (-1)

'''l = []
    
for j in range (2, N) : 
    if j in nprime and N - j in nprime :
        l.append((j, abs(j - (N - j))))
    
l.sort(key = lambda x : x[1])
rst[0], rst[1] = l[0][0], N - l[0][0]

N = copy_N - N
l.clear()

for j in range (2, N) : 
    if j in nprime and N - j in nprime :
        l.append((j, abs(j - (N - j))))

l.sort(key = lambda x : x[1])
rst[2], rst[3] = l[0][0], N - l[0][0]

rst.sort()

print (rst)'''
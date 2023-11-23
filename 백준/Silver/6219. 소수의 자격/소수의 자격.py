import math

A, B, D = map(int, input().split())

finder = 0

def eratosthenes (M, N) : # 0은 소수, 1은 합성수
    nums = [0 for i in range (N + 1)]
    nums.insert(0, 1)
    
    for i in range (2, int(math.sqrt(N) + 1)) : 
        if nums[i] == 0 :
            for j in range (i + i, N + 1, i) :
                nums[j] = 1
    
    return nums[M : ]
    
slist = eratosthenes(A, B)
for i in range (B - A + 1) : 
    if slist[i] == 0 : # 소수면
        if str(D) in list(str(i + A)) : # 소수인 수 안에 D가 들어있으면
            if str(i + A) != '1': # 1이 아니라면 (1은 소수 아님)
                finder += 1
            
print (finder)
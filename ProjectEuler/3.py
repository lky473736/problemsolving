import sys
import math

# def eratosthenes (M, N) :
#     nums = [0 for i in range (N + 1)]
#     nums.insert(0, 1)

#     for i in range (2, int(math.sqrt(N) + 1)) : 
#         if nums[i] == 0 :
#             for j in range (i + i, N + 1, i) :
#                 nums[j] = 1

#     return nums[M : ]

# prime = eratosthenes(1, 600851475143)[:-1]
# prime = [idx+1 for idx in range (1, 600851475143) if prime[idx] == 0]
# prime_set = set(prime)

# print (prime)

# for num in prime[::-1] : 
#     if 600851475143 % num == 0 : 
#         print ("eureka! : " num)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

factor = 1
num = 600851475143
nlist = []

while factor**2 < num : 
    if num % factor == 0 : 
        nlist.append (factor)
        nlist.append (num // factor)
    factor += 1
        
print (nlist)
nlist.sort(reverse=True)

# prime = eratosthenes(1, 8462696833)[:-1]
# prime = [idx+1 for idx in range (1, 8462696833) if prime[idx] == 0]
# prime_set = set(prime)

for compo in nlist : 
    if is_prime(compo) :
        print ("eureka! : ", compo)

'''
[1, 600851475143, 71, 8462696833, 839, 716151937, 1471, 408464633, 6857, 87625999, 59569, 10086647, 104441, 5753023, 486847, 1234169]
eureka! :  6857
eureka! :  1471
eureka! :  839
eureka! :  71
'''

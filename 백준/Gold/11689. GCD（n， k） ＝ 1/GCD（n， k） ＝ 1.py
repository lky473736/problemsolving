'''
    GCD(n, k) == 1
    => 서로소를 의미
'''

n = int(input())
ans = n

for i in range(2, int(n**0.5) + 1) :
    if n % i == 0 :
        while n % i == 0 :   
            n //= i
        ans *= (1 - (1 / i))

if n > 1 : # 만약 내가 소수면
    ans *= (1 - (1 / n))

print (int(ans))
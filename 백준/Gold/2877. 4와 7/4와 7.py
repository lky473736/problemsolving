import sys

# 4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 777, 4444...
# https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2877-4%EC%99%80-7-%EA%B5%AC%ED%98%84

K = int(sys.stdin.readline())

if K == 1 : 
    print (4)
    exit()
    
else : 
    binary = format(K+1, 'b')[1:]
    print(binary.replace('0', '4').replace('1', '7'))

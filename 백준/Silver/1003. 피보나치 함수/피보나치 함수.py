'''int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}'''

'''import sys

def fibonacci (n, original) :
    global num_0
    global num_1
    
    if n == original : 
        num_0 = 0
        num_1 = 0

    if n == 0 :
        num_0 += 1
        return 0
        
    elif n == 1 :
        num_1 += 1
        return 1
        
    else :
        return fibonacci(n-1, n) + fibonacci(n-2, n)
        
T = int(sys.stdin.readline())

for _ in range (T) :
    N = int(sys.stdin.readline())
    
    fibonacci(N, N)
    print (num_0, num_1)
    
    num_0 = 0
    num_1 = 0'''

import sys

T = int(sys.stdin.readline())

for _ in range (T) : 
    N = int(sys.stdin.readline())
    
    a, b = 1, 0
    
    while N != 0 :
        temp = a
        a = b
        b = temp + b
        
        N -= 1
        
    print (a, b)
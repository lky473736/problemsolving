import itertools

def euclidean(X, Y):
    a = Y
    b = X % Y
    p = 0

    if b == 0:
        return a

    while True:
        p = a % b

        if p == 0:
            break

        a = b
        b = p

    return b

N = int(input())

for i in range(N):
    slist = list(map(int, input().split()))
    permu = itertools.permutations(slist, 2)
    maxgcd = 0  # Initialize maxgcd to find maximum

    for j in permu:
        gcd = euclidean(j[0], j[1])

        if gcd > maxgcd:
            maxgcd = gcd

    print(maxgcd)
import sys

T = int(sys.stdin.readline())

for _ in range (T) :
    lst = list(map(int, sys.stdin.readline().split()))
    lst.sort(reverse = True)
    print (lst[2])
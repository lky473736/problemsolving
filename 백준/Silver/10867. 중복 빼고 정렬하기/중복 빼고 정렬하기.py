N = int(input())
lst = list(set(list(map(int, input().split()))))

lst.sort()

print (*lst)
# hello jung in

N, M = map(int, input().split())
cardlist = list(map(int, input().split()))

cardlist.sort(reverse = True)

max_sum = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            current_sum = cardlist[i] + cardlist[j] + cardlist[k]
            if current_sum <= M:
                max_sum = max(max_sum, current_sum)

print (max_sum)
import sys

N, K = map(int, sys.stdin.readline().split())
numlist = []

for i in range(N):
    score = float(sys.stdin.readline())
    numlist.append(score)

numlist.sort()

js = sum(numlist[K:N-K]) / (N - K * 2)
bs = (sum(numlist[K:N-K]) + numlist[K] * K + numlist[N-K-1] * K) / N

print("%.2f" % (js + 1e-8))
print("%.2f" % (bs + 1e-8))
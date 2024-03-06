import sys

n = int(sys.stdin.readline())
a = (1 + n) * n // 2
print ((3 * a + n + 1) %45678)
import sys
import math

b, c, a1, a2 = map(int, sys.stdin.readline().split())

print ((b + math.sqrt(b**2 + 4*c)) / 2)
from collections import Counter
import sys

N = int(sys.stdin.readline())
list_book = []

for _ in range (N) :
    list_book.append(sys.stdin.readline().rstrip())

counts = Counter(list_book)
counts = [(i, counts[i]) for i in counts.keys()]
counts.sort(key = lambda x : (-x[1], x[0]))
print (counts[0][0])
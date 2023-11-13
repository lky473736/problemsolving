# https://yeomss.tistory.com/290
import sys
from collections import deque

input = sys.stdin.readline().rstrip()
N = int(input)

card = deque([i for i in range (1, N + 1)])

while len(card) != 1 :
    card.popleft()
    card.rotate(-1)

print (card[0])
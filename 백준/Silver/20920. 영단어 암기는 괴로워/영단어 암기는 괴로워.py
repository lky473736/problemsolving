import sys

N, M = map(int, sys.stdin.readline().split())

counting = dict()
length = dict()

for _ in range (N) :
    word = sys.stdin.readline().rstrip()
    
    if len(word) >= M :
        try :
            counting[word] += 1
            
        except KeyError :
            counting[word] = 1
            length[word] = len(word)

words = list(counting.keys())
words.sort (key = lambda x : (-counting[x], -length[x], x))

for compo in words :
    print (compo)
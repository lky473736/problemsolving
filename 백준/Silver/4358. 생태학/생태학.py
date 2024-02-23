import sys
from collections import defaultdict

dictionary = defaultdict(int)
counting = 0

while True :
    line = sys.stdin.readline().rstrip()
    
    if not line :
        break
    
    dictionary[line] += 1
    counting += 1

dictionary = dict(sorted(dictionary.items()))

for i in dictionary.keys() :
    print (i, "%.4f" % ((dictionary[i]/counting)*100))

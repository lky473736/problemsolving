import itertools
import sys

N = int(sys.stdin.readline())

for i in itertools.permutations([str(i + 1) for i in range(N)]) :
    compo = ' '.join(i)
    print (compo)
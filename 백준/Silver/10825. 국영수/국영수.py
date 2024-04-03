import sys

N = int(sys.stdin.readline())
dicta = dict()
lista = list()

for _ in range (N) :
    name, kor, eng, math = sys.stdin.readline().rstrip().split()
    dicta[name] = [int(kor), int(eng), int(math)]
    lista.append ([name, int(kor), int(eng), int(math)])
    
lista.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for compo in lista : 
    print (compo[0])
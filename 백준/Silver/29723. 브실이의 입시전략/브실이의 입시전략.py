import sys

N, M, K = map(int, sys.stdin.readline().split())

dict_subject = dict()
suma = 0

for _ in range (N) :
    subject, score = sys.stdin.readline().rstrip().split()
    score = int(score)
    dict_subject[subject] = score
    
for _ in range (K) : 
    subject_open = sys.stdin.readline().rstrip()
    suma += dict_subject[subject_open]
    del dict_subject[subject_open]
    
if M == K : 
    print (suma, suma)
    
else :
    min_score, max_score = suma, suma
    list_restval = sorted(dict_subject.values())
    
    for i in range (M-K) : 
        min_score += list_restval[i]
        max_score += list_restval[-1-i]
        
    print (min_score, max_score)
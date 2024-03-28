import sys

N, M = map(int, sys.stdin.readline().split())

scores = list(map(int, sys.stdin.readline().split()))

student = [-1, -1]

for i in range (M) :
    compo = list(sys.stdin.readline().split())
    compo[0] = int(compo[0])
    
    student_score = 0
    
    for j in range (1, N+1) :
        if compo[j] == 'O' :
            student_score += scores[j-1] 
            
    if student == [-1, -1] : 
        student = [compo[0], student_score]
        
    else :
        if student[1] < student_score :
            student = [compo[0], student_score]
            
        elif student[1] == student_score :
            if student[0] > compo[0] :
                student[0] = compo[0]
                
    # print (student)
                
print (*student)
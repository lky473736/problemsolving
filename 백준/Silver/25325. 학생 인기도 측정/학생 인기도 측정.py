import sys

n = int(sys.stdin.readline())

student_dict = dict()
student_list = list(sys.stdin.readline().rstrip().split())

for key in student_list :
    student_dict[key] = 0
    
for i in range (n) :
    inp = list(sys.stdin.readline().rstrip().split())
    
    for compo in inp : 
        student_dict[compo] += 1
        
student_list = [[key, student_dict[key]] for key in student_list]

student_list.sort(key = lambda x : (-x[1], x[0]))

for compo in student_list :
    print (compo[0], compo[1])
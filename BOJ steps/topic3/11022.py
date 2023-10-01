T = int(input())
slist = []
klist = []

for i in range(T):
    A, B = map(int, input().split())
    slist.append(A + B)
    klist.append(A)
    klist.append(B)

for j in range(T):  # j 변수 초기화를 루프 밖으로 이동
    print(f'Case #{j + 1}: ' 
    + str(klist[2*j]) + ' + ' + str(klist[2*j+1])
    + ' = ' + str(slist[j]))

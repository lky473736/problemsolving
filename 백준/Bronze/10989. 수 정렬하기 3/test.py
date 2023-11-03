import sys

N = int(input())  
max_value = 10000  # 가장 큰 입력 값 범위를 설정
counting = [0] * (max_value + 1)

for i in range(N):
    input_value = int(input())  
    counting[input_value] += 1

for i in range(max_value + 1):
    while counting[i] > 0:
        print(i)


'''import sys

N = int(input())
slist = []

for i in range(N):
    slist.append(int(sys.stdin.readline()))

finder = [0 for j in range (max(slist) - min(slist) + 1)]
    
for k in slist : 
    finder[k - min(slist)] += 1
    
for n in range (len(finder)) :
    if finder[n] != 0 :
        for b in range (finder[n]) :
            print (min(slist) + n)
'''

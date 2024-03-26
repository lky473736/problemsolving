'''
문제
최근에, JOI 대학 정보학과에서 입학 시험이 진행되었습니다. 시험은 만점이고, n 명의 학생이 응시했습니다. JOI 대학에서는 최저 합격 점수를 결정하기 위해 시험 결과를 바탕으로 각 학생에게 순위를 매기기로 했습니다.

n 명의 학생의 점수가 주어졌을 때, 각 학생의 순위를 구하는 프로그램을 작성하십시오. 단, 동일한 점수의 학생이 있는 가능성이 있음에 유의하십시오.

입력
입력의 첫 번째 줄에는 학생 수 n (1 ≤ n ≤ 100000) 이 씌여 있습니다. 이어지는 n 개의 줄은 학생의 점수를 나타냅니다. i + 1 (1 ≤ i ≤ n) 번째 줄에는 응시 번호 i의 학생의 점수 si (0 ≤ si ≤ 100) 가 씌여 있습니다.

출력
출력은 표준 출력으로 이루어집니다. 출력은 n 줄로 구성됩니다. i 번째 줄 (1 ≤ i ≤ n) 에는 응시 번호 i의 학생의 순위를 출력하십시오.
'''

import sys

n = int(sys.stdin.readline())

seta = set()
lsta = list()

for i in range (n) :
    compo = int(sys.stdin.readline())
    lsta.append (compo)
    seta.add (compo)

sorted_lsta = sorted(list(seta), reverse = True)

score = 1
scorelist = [0 for i in range (n)]

for i in sorted_lsta :
    counting = 0
    
    for j in range (n) :
        if lsta[j] == i :
            scorelist[j] = score
            counting += 1
            
    score += counting
'''
score = 1
scorelist = [0 for i in range (n)]

for key in sorted_dict.keys() :
    counting = 1
    
    for '''

for i in scorelist : 
    print (i)
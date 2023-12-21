'''
   팀의 개수 n, 문제의 개수 k, 당신 팀의 ID t, 로그 엔트리의 개수 m
   팀 ID i, 문제 번호 j, 획득한 점수 s
   
   1) 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높다. 
   2) 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높다. 
'''

T = int(input())

for _ in range (T) :
    n, k, t, m = map(int, input().split()) # 팀 갯수, 문제 갯수, 내 팀, 로그 엔트리
    
    counting = [0 for i in range (n)] # 제출 횟수
    scorelist = [[0 for j in range (k)] for i in range (n)]
    finalpoint = [0 for i in range (n)]
    
    for procedure in range (m) : 
        log = list(map(int, input().split())) # i, j, s
        
        counting[log[0]-1] += 1
        
        if scorelist[log[0]-1][log[1]-1] < log[2] : 
            scorelist[log[0]-1][log[1]-1] = log[2]
        
        finalpoint[log[0]-1] = procedure
        
    score = [[sum(scorelist[i]), counting[i], finalpoint[i], i+1] for i in range(n)] # 최종 점수, 풀이 제출 횟수, 마지막 제출시간
    
    score.sort(key=lambda x: (-x[0], x[1], x[2]))

    print ([score[i][3] for i in range (n)].index(t) + 1)
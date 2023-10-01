N = int(input())
lie_score_list = []

fucked_score_list = list(map(int, input().split()))
M = max(fucked_score_list)

for i in fucked_score_list :
    lie_score_list.append (i / M * 100)
    
print (sum(lie_score_list)/N)

import sys

N, M = map(int, sys.stdin.readline().split())

idol = []

for i in range (N) :
    group_name = sys.stdin.readline().rstrip()
    member_count = int(sys.stdin.readline())
    group_members = []
    
    for j in range (member_count) :
        member_name = sys.stdin.readline().rstrip()
        group_members.append(member_name)
        
    idol.append ([group_name, member_count, sorted(group_members), set(group_members)])

for i in range (M) :
    word = sys.stdin.readline().rstrip()
    gamenum = int(sys.stdin.readline())
    
    if gamenum == 0 :
        for group in idol :
            if word == group[0] :
                for member in group[2] : 
                    print (member)
                    
    else :
        for group in idol :
            if word in group[3] :
                print (group[0])
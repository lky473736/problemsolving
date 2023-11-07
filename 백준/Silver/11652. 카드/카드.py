'''slist = []
clist = []

N = int(input())

for i in range (N) :
    com = int(input())
    slist.append (com)

for j in range (N) :
    clist.append (slist.count(slist[j]))
    
maxc = max(clist)
    
if clist.count(maxc) >= 2 :
    finder = []
    for k in clist :
        if k == maxc :
            finder.append(slist[clist.index(k)])
    
    print(min(finder))
   
else :
    print(slist[clist.index(maxc)])'''
    
slist = []
N = int(input())

for i in range(N):
    com = int(input())
    slist.append(com)

max_num = None  # 가장 많이 등장한 숫자
max_count = 0  # 가장 많이 등장한 숫자의 등장 횟수

count_dict = {}  # 숫자의 등장 횟수를 저장하는 딕셔너리

for num in slist:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

    if count_dict[num] > max_count or (count_dict[num] == max_count and num < max_num):
        max_count = count_dict[num]
        max_num = num

print(max_num)
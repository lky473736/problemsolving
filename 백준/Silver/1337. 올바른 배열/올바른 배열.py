# no nested

import sys 

N = int(sys.stdin.readline().rstrip())

slist = []
differ = []

for i in range (N) : # 요소 넣기
    c = int(sys.stdin.readline().rstrip())
    slist.append(c)
    
slist.sort()

def finddiffer (nlist, N) :
    differ = []
    
    for j in range (1, N) : # 차이 리스트 구하기
        difference = nlist[j] - nlist[j-1]
        differ.append (difference)
    
    return differ
    
def check_sublist(main_list, sublist):
    # 리스트에서 일정 부분을 확인하는 함수
    if len(sublist) == 0:
        return True  # 부분 리스트가 비어 있으면 언제나 True 반환

    for i in range(len(main_list)):
        if main_list[i:i+len(sublist)] == sublist:
            return True

    return False

differ = finddiffer(slist, N)

if check_sublist(differ, [1, 1, 1, 1]) :
    print (0)
    exit()
    
else :
    finder = []
    
    for l in range (len(slist)) : 
        n = 0
        i = slist[l] # slist[0]
        new_differ = []
        fslist = slist[:]
        
        while check_sublist(new_differ, [1, 1, 1, 1]) == False :
            if i not in fslist : 
                fslist.append (i)
                fslist.sort()
                new_differ = finddiffer(fslist, len(fslist))

                n += 1
                
            i += 1
    
        finder.append (n)

    print (min(finder))
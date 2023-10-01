'''st_list = []

for i in range (29) :
    st_list.append (i + 1)
    
yes_hw_list = []
no_hw_list = []

for j in range (28) : 
    st = int(input())
    yes_hw_list.append (st)

yes_hw_list.sort()
    
for k in range (len(st_list)) : 
    if k + 1 in yes_hw_list :
        pass
    
    else : 
        no_hw_list.append (k + 1)
        
for m in no_hw_list :
    print (m)
    '''
st_list = list(range(1, 31))
yes_hw_list = []

# 28명의 학생이 제출한 과제를 입력받습니다.
for j in range(28):
    st = int(input())
    yes_hw_list.append(st)

yes_hw_list.sort()

no_hw_list = []

# 제출하지 않은 학생 번호를 찾습니다.
for k in st_list:
    if k not in yes_hw_list:
        no_hw_list.append(k)

# 출력
for m in no_hw_list:
    print(m)

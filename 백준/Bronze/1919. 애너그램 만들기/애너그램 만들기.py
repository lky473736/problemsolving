'''A = input()
B = input()

Alist = []
Blist = []

count = 0

for i in A :
    Alist.append (i)
    
for j in B : 
    Blist.append (j)

Aset = set(Alist)
Bset = set(Blist)

symmetricdifference = Aset.union(Bset) - Aset.intersection(Bset)

if len(symmetricdifference) == 0 :
    print (0)
    exit()

for i in symmetricdifference :
    if i in Alist : 
        count += Alist.count(i)
        
    else : 
        count += Blist.count(i)
        
print (count)'''

A = input()
B = input()

A_count = [0] * 26  # 알파벳 개수를 저장할 리스트 초기화
B_count = [0] * 26

# 문자열 A의 각 알파벳 개수를 세기
for char in A:
    A_count[ord(char) - ord('a')] += 1

# 문자열 B의 각 알파벳 개수를 세기
for char in B:
    B_count[ord(char) - ord('a')] += 1

# 두 문자열에서 필요한 최소 문자 제거 수 계산
removal_count = 0
for i in range(26):
    removal_count += abs(A_count[i] - B_count[i])

print(removal_count)
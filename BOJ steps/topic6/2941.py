'''croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 다 두 글자

word = input()
croatia_count = 0

for i in croatia : 
    if i in word : 
        count = word.count(i)
        croatia_count += count
        word = word.replace(i, ' ')  # word에서 해당 크로아티아 알파벳을 모두 제거
        
word = word.replace (' ', '')

not_croatia_wordset = set(word)  # 크로아티아 알파벳을 제거한 문자열을 집합으로 변환하여 중복을 제거

total_count = len(not_croatia_wordset) + croatia_count  # 중복을 제거한 문자열 길이와 크로아티아 알파벳 개수를 합하여 총 개수를 구함
print(total_count)'''

# 문제 잘 읽자...
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 다 두 글자

word = input()
croatia_count = 0

for i in croatia : 
    if i in word : 
        count = word.count(i)
        croatia_count += count
        word = word.replace(i, ' ')  #  word에서 해당 크로아티아 알파벳을 모두 제거
        
word = word.replace (' ', '')

total_count = len(word) + croatia_count  
print(total_count)

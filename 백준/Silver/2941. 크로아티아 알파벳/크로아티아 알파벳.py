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
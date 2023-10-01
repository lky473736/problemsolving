# 글자 수, 바이트 계산기

print ("한글 문장의 글자 수, 바이트 계산기를 시작합니다.")
sentence_number = int(input("문장 수를 입력해주세요. : "))
sentence_list = []
sum_len = 0

for i in range (sentence_number) :
    word = input("한글을 입력 : ")
    sentence_list.append(word)
    
for j in range (sentence_number) : 
    sum_len = sum_len + len(sentence_list[j])
    
print ("글자 수는 : ", sum_len)
print ("byte : ", 2 * sum_len)

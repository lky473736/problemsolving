# 10진수의 n의 자리에 존재하는 0의 갯수 counting

val = input("10진수를 입력하시오. : ") # input example) val = 100

numberlist = []
whilecountingnumber = 0
zeronumber = 0

for i in range (len(val)) : # len(val) = 3
    numberlist.append (val[i])

print ("numberlist : ", numberlist)
print ("입력값의 길이 : ", len(val))

while whilecountingnumber < len(val) :    
    if numberlist[whilecountingnumber] == '0' : # 리스트를 차례대로 탐색하면서 0 찾음
        zeronumber = zeronumber + 1
        
    whilecountingnumber = whilecountingnumber + 1
    
print ("0의 갯수 : ", zeronumber)

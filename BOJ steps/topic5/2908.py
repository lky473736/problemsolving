A, B = input().split()

# https://codechacha.com/ko/python-reverse-string/
# 문자열 뒤집기 위해선 [::-1]

rev_A = int(A[::-1])
rev_B = int(B[::-1])

if rev_A < rev_B : 
    print (rev_B)
    
elif rev_A > rev_B :
    print (rev_A)

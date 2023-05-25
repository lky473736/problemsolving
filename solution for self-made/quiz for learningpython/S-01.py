# fibonacci sequence

i = 0
N = int(input("수를 입력하시오 : "))
a = 1 
sequence = []

print (a)

while i < N - 1 : # n개의 피보나치 수열이 출력되게끔 n번 반복
    print (a)
    sequence.append (a)
    a = sequence[i-1] + sequence[i]
    i = i + 1

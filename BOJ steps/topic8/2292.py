# difference sequence
# https://j1w2k3.tistory.com/m/717
# https://ooyoung.tistory.com/82
# https://m.blog.naver.com/sunghak93/222498618974

'''N = int(input())

slist = [[1]]

startingpoint = 2
i = 1

# find floor
while True :
    slist.append (list(range (startingpoint, startingpoint + 6 * i - 1 + 1)))
    startingpoint = startingpoint + 6 * i - 1 + 1
    
    i += 1
    
    if N in slist[-1] :
        break

floor = len(slist)
    
print (floor)''' # -> 메모리 에러

n = int(input())

m = 0                   # 각 칸의 끝 방번호가 6x1,6x2,6x3,6x4...이 순으로 증가
end_num = 1             # 끝 방번호를 의미하는 end_num 변수와 6을 곱해줄 m 변수 선언

if n == 1:              # m + 1로 출력하기에 n이 1일 경우 2가 출력된다. 따라서 예외처리
	print(n)
else:
	while True:        # m의 숫자가 증가하면서 끝 방번호를 높여준다.
		a = 6 * m      # 칸 수가 증가할 때마다 끝 방번호의 증가하는 수를 담은 변수 a 선언
		end_num += a   # 끝 방번호를 증가 시켜준다.
		if end_num >= n: # 끝 방번호가 n보다 크다면 n은 그 끝방번호 칸 안에 존재한다는 소리
			print(m+1)   # 그래서 m+1 증가한 칸의 수를 출력해주면 몇 칸 이동했는지 유추가능 
			break        # 무한루프 탈출
		m += 1           # 반복문 돌때마다 6에 곱해줄 m 1씩 증가

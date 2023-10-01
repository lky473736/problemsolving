''' https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
sys.stdin.readline : 반복문으로 여러줄을 입력받는 상황에서는 반드시 sys 사용해야 시간초과 안남
* 이때 개행문자 또한 readline 하기 때문에 rstrip이 필요함

'''
import sys

T = int(input())
slist = []

for i in range (T) : 
    A, B = map(int, sys.stdin.readline().rstrip().split())
    slist.append (A + B)

for j in slist : 
    print (j)

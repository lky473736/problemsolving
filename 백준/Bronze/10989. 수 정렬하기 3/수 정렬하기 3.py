N = int(input())
counting = [0] * 10001  # 1부터 10,000까지의 범위를 고려하여 크기를 10,001로 설정

for i in range(N):
    num = int(input())
    counting[num] += 1

# counting 배열을 기반으로 정렬된 결과를 출력
for i in range(len(counting)):
    for j in range(counting[i]):
        print(i)


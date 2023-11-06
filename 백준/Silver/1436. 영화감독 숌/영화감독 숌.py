N = int(input())

point = 665  # Start from 665 to find the first number containing '666'

for i in range(N):
    while True:
        point += 1

        if '666' in str(point):
            break

print(point)

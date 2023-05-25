# 기억하자. remove나 del 한 후에는 인덱스가 변경된다.

stack = []

for i in range(10):
    component = input("입력: ")
    stack.append(component)

print(stack)

for k in range(len(stack)):
    delq = int(input("0을 입력하면 remove: "))
    if delq == 0:
        del stack[0]
        print(stack)

import sys

def add(S, n):
    if n not in S:
        S.append(n)

def remove(S, n):
    if n in S:
        S.remove(n)

def check(S, n):
    result = 1 if n in S else 0
    print(result)

def toggle(S, n):
    if n in S:
        S.remove(n)
    else:
        S.append(n)

N = int(sys.stdin.readline().strip())
S = []

for i in range(N):
    order = sys.stdin.readline().strip().split()

    if len(order) == 2:
        command, argument = order
        argument = int(argument)

        if command == 'add':
            add(S, argument)
        elif command == 'remove':
            remove(S, argument)
        elif command == 'check':
            check(S, argument)
        elif command == 'toggle':
            toggle(S, argument)
    else:
        command = order[0]

        if command == 'all':
            S = list(range(1, 21))
        elif command == 'empty':
            S = []
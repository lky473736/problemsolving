'''
a, b, n, w = map(int, input().split())

if a == b:
    if b == w // n:
        if w % (a * 2) == 0:
            print(w // (a * 2), w // (a * 2))
        else:
            print(-1)
    else:
        print(-1)
else:
    if (w - b * n) % (a - b) != 0:  # 나머지가 0이 아닐 때
        print(-1)
    else:
        x = (w - b * n) // (a - b)
        if x < 0 or x > n:  # x가 음수이거나 n보다 클 때
            print(-1)
        else:
            print(x, n - x)
''''''
a, b, n, w = map(int, input().split())

if a == b and b == w//n :
    if a == b : # a랑 b랑 같으면 
        if w % (a*2) == 0 :
            print (w // (a*2), w // (a*2))
            exit()
    print (-1)
    
elif a == b and b != w//n :
    print (-1)
    
else : 
    if (w-b*n)//(a-b) == 0 : # x가 0
        print (-1)
        exit()
    print ((w-b*n)//(a-b), n-(w-b*n)//(a-b)) 
'''

a, b, n, w = map(int, input().split())

cnt = 0
y, ys = 0, 0

for i in range(1, n):
    if a * i + b * (n - i) == w:
        cnt += 1
        y = i
        ys = n - i

if cnt != 1:
    print(-1)
else:
    print(y, ys)

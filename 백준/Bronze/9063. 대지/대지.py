N = int(input())

xlist, ylist = [], []

for i in range (N) :
    x, y = map(int, input().split())
    xlist.append (x)
    ylist.append (y)

xlen = sorted(xlist)[-1] - sorted(xlist)[0]
ylen = sorted(ylist)[-1] - sorted(ylist)[0]

print (xlen * ylen)
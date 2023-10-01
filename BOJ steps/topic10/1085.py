x, y, w, h = map(int, input().split())

po1 = abs(x)
po2 = abs(y)
po3 = abs(w - x)
po4 = abs(h - y)

finder = [po1, po2, po3, po4]

print (sorted(finder)[0])

n = int(input())

if n == 1 :
    print (4)
    exit()

top_bottom = 1 + n
side = n * 2
half = (n - 1) * 2 * (1/2)

print (int(top_bottom + side + half))
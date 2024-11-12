import sys

n = int(sys.stdin.readline())
slist = list(map(int, sys.stdin.readline().split()))

# if n == 1:
#     print(0)
# else:
#     total_sum = sum(slist) 
#     adj_sum = sum(slist[i] * slist[i + 1] for i in range(n - 1))

#     rst = slist[0] * slist[-1] + adj_sum

#     print(rst)

temp = sum(slist)

rst = 0
for i in range (n-1) :
    temp -= slist[i]
    rst += temp * slist[i]
    
print (rst)
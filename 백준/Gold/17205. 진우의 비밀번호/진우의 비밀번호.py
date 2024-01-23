N = int(input())
pwd = input()
ans = 0
anum = ord('a')
N -= 1 # first starting 

for alphabet in pwd:
    difference = ord(alphabet) - anum
    if difference > 0:
        ans += (difference) * 26 * (26 ** N-1)// (25) + difference
    ans += 1
    N -= 1
    
print (ans)
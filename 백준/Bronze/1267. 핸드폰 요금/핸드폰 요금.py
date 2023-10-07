'''N = int(input())
calllist = list(map(int, input().split()))

ylist = []
mlist = []
count = 1
index = 0
section = 0

# youngsik
while True : 
    if section <= calllist[index] < section + 30 :
        ylist.append (count)
        
        if index != N - 1 :
            index += 1
        
        else :
            break
    
    else : 
        count += 1
        section += 30
    
count = 1
index = 0
section = 0

# minsik
while True : 
    if section <= calllist[index] < section + 60 :
        mlist.append (count)
        
        if index != N - 1 :
            index += 1
        
        else :
            break
    
    else : 
        count += 1
        section += 60
        
youngsik = sum(ylist) * 10
minsik = sum(mlist) * 15

print (youngsik)
print (minsik)

if youngsik < minsik:
    print(f"Y {youngsik}")
    
elif youngsik > minsik:
    print(f"M {minsik}")
    
else:
    print(f"Y M {youngsik}")'''
    
N = int(input())
calllist = list(map(int, input().split()))

youngsik = 0
minsik = 0

for i in calllist : 
    youngsik += ((i // 30) + 1) * 10
    minsik += ((i // 60) + 1) * 15
    
if youngsik < minsik:
    print(f"Y {youngsik}")
    
elif youngsik > minsik:
    print(f"M {minsik}")
    
else:
    print(f"Y M {youngsik}")
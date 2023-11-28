# set에서는 append가 아니라 add : https://m.blog.naver.com/sw4r/221544216284

N = int(input())

rainbow = set()
rainbowmode = 0

for i in range (N) : 
    compoa, compob = input().split()
    if rainbowmode == 0 : 
        if compob == "ChongChong" or compoa == "ChongChong" : 
            rainbow.add (compob)
            rainbow.add (compoa)
            rainbowmode = 1
            
    else : # ChongChong time
        if compoa in rainbow or compob in rainbow : 
            rainbow.add (compoa)
            rainbow.add (compob)
            
print (len(rainbow))
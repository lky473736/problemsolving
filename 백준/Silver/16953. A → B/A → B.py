import sys

A, B = map(int, sys.stdin.readline().split())

if str(B)[-1] != '1' and B % 2 != 0 : 
    print (-1)
    exit()

cnt = 1
while True :
    # print (A, B)
    
    if A > B : 
        print (-1)
        break
    
    else : 
        if A == B : 
            print (cnt)
            break
        
        else : 
            slist = [compo for compo in str(B)]
            # print (slist)
            if slist[-1] == '1' : 
                slist.pop()
                # print ('1뺌')

                B = int(''.join(slist))
                cnt += 1
                    
            else : 
                if B % 2 == 1 : 
                    print (-1)
                    exit()
                    
                # print ('2나눔')
                B //= 2
                cnt += 1

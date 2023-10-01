dice1 = [1, 2, 3, 4, 5, 6]
dice2 = dice1
dice3 = dice1

oddlist = []

counting_all = 0
counting_odd = 0

for i in dice1 :
    for j in dice2 : 
        for k in dice3 : 
            counting_all += 1
            print ([i, j, k])
            
            if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 :
                counting_odd += 1
                oddlist.append ([i, j, k])

print ("-" * 10)

for n in oddlist :
    print (n)
    
print ("모든 경우의 수 : ", counting_all) 
print ("세 주사위가 동시에 홀수가 되는 경우의 수 : ", counting_odd)
print ("확률 : ", counting_odd / counting_all)

# stop diablo

N = int(input())
price = []

for i in range (N) :
    price_com = int(input())
    price.append (price_com)
    
for j in price : 
    quarter = j // 25
    j = j % 25
    
    dime = j // 10
    j = j % 10
    
    nickel = j // 5
    j = j % 5
    
    penny = j // 1 
    
    print (quarter, dime, nickel, penny)

num_list = []
rest_list = []

for i in range (10) : 
    num = int(input())
    num_list.append (num)
    
for j in num_list :
    rest_list.append (j % 42)
    
rest_set = set (rest_list)
print (len(rest_set))

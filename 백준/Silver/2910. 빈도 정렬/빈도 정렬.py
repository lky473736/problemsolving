import sys

N, C = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr_set = set()
arr_order_lst = []

for i in arr :
    if i in arr_set :
        pass
    
    else :
        arr_set.add(i)
        arr_order_lst.append (i)
        
arr_dict = {i : arr.count(i) for i in arr_set}

arr_order_lst_copy = arr_order_lst.copy()
arr_order_lst.sort (key = lambda x : (-arr_dict[x], arr_order_lst_copy))

for i in arr_order_lst : 
    for k in range (arr_dict[i]) :
        print (i, end = " ")
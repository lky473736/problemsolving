def bubble_sort(lst) :
    n = len(lst)
    for i in range(n - 1) :
        for j in range(n - i - 1) :
            if lst[j] > lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(f"사이클 {i + 1}: {lst}")
    return lst

lst = [0, 183, 2, 93821, -32, 543, 542, 1]
sorted_lst = bubble_sort(lst)
print("버블 정렬 완료 : ", sorted_lst)

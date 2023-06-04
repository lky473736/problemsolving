# 정렬 알고리즘을 사용하면 된다
# https://ko.wikipedia.org/wiki/%EC%A0%95%EB%A0%AC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98#%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%98_%EB%B9%84%EA%B5%90
 
# 본 코드에서는 'quiz for endterm - learningpython' 15제에서 만들었던 버블 정렬 코드를 사용한다.

def ssort(lst) :
    n = len(lst)
    for i in range(n - 1) :
        for j in range(n - i - 1) :
            if lst[j] > lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

lst = [0, 183, 2, 93821, -32, 543, 542, 1]

print (list(ssort(lst)))
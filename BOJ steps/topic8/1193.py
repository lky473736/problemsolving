# find fraction https://speckofdust.tistory.com/150
# list reverse : https://codingpractices.tistory.com/entry/Python-reverse-reversed-%EC%82%AC%EC%9A%A9%EB%B2%95%EA%B3%BC-%EC%B0%A8%EC%9D%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0

X = int(input())

slist = [[1]]

start, p = 2, 1

while True : 
    if X in slist[-1] :
        break
    
    if p % 2 != 0 :
        slist.append (list(range(start, start + p + 1)))
    
    else :
        slist.append (list(reversed(list(range(start, start + p + 1)))))
        
    start = start + p + 1
    
    p = p + 1

numerator = slist[p - 1].index(X) + 1
denominator = p - slist[p - 1].index(X)
    
print (str(numerator) + '/' + str(denominator))

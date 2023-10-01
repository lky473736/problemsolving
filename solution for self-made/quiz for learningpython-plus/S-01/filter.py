def sfilter(condition, iterable) :
    result = []
    
    for item in iterable :
        if condition(item) :
            result.append(item)
            
    return result

def condition(x) :
    return x < 2

print(list(sfilter(condition, [0, 1, 2, 3, 4])))

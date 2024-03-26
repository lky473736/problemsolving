import sys

N = int(sys.stdin.readline())
user = set()
dict_task = dict()

for i in range (N) :
    name, task, point = map(str, sys.stdin.readline().rstrip().split())
    point = int(point)
    
    if name not in user :
        user.add (name)
        dict_task[name] = {task : point}
        
    else :
        try :
            if dict_task[name][task] < point :
                dict_task[name][task] = point
        
        except : 
            dict_task[name][task] = point

result = []

for name in list(user) :
    result.append([name, sum(dict_task[name].values())])
    
result.sort(key = lambda x : (-x[1]))

for compo in result :
    print (*compo)
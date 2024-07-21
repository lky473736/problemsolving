# import sys

# work = {
#     'Re' : 0,
#     'Pt' : 0, 
#     'Cc' : 0,
#     'Ea' : 0,
#     'Tb' : 0,
#     'Cm' : 0, 
#     'Ex' : 0
# }

# keys = work.keys()
# cnt = 0

# while True : 
#     try : 
#         row = list(sys.stdin.readline().split())
#         print (row)
        
#         for compo in row : 
#             print (compo)
#             work[compo] += 1
#             cnt += 1
        
#     except : 
#         break
    
# for key in keys : 
#     print (f'{key} {work[key]} {"{:.2f}".format(work[key] / cnt)}')
    
# print (f'Total {cnt} 1.00')

import sys

work = {
    'Re': 0,
    'Pt': 0, 
    'Cc': 0,
    'Ea': 0,
    'Tb': 0,
    'Cm': 0, 
    'Ex': 0
}

keys = work.keys()
cnt = 0

while True: 
    try: 
        row = list(sys.stdin.readline().split())
        if not row:  # EOF를 만나면 break
            break
        
        for compo in row: 
            if compo in work:  # 유효한 키만 처리
                work[compo] += 1
            
            cnt += 1
        
    except Exception as e:
        # print(f"Error: {e}")
        break

for key in keys: 
    print(f'{key} {work[key]} {"{:.2f}".format(work[key] / cnt) if cnt > 0 else "0.00"}')

print(f'Total {cnt} 1.00')
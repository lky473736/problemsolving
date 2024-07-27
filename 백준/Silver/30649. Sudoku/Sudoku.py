'''
<문제>
스도쿠는 논리 기반의 조합적 숫자 배치 퍼즐입니다. 목표는 9 × 9 그리드를 1부터 9까지의 숫자로 채우는 것이며, 다음 조건이 만족되어야 합니다:

각 행에는 1부터 9까지의 숫자가 정확히 한 번씩 나타나야 합니다.
각 열에는 1부터 9까지의 숫자가 정확히 한 번씩 나타나야 합니다.
각 3 × 3 하위 그리드에는 1부터 9까지의 숫자가 정확히 한 번씩 나타나야 합니다.
주어진 미완성 스도쿠 그리드에서 오류가 있는지 확인하세요.
참고: 스도쿠 그리드가 풀 수 있는지는 확인할 필요가 없습니다.

<입력>
입력은 스도쿠 그리드를 설명합니다.
문자 ’|’, ’-’, ’+’는 3 × 3 하위 그리드를 구분하는 프레임을 형성합니다.
문자 ’.’는 빈 셀을 나타냅니다.
나머지 문자는 ’1’부터 ’9’까지의 숫자입니다.
'''

import sys

first_row = sys.stdin.readline()
datas = list()

for i in range (3) : 
    for j in range (3) :
        # print (i)
        
        rows = list(sys.stdin.readline().rstrip().split('|'))
        row = list(rows[1] + rows[2] + rows[3])
        
        for k in range (9) :
            if row[k] == '.' :
                row[k] = 0
                        
            else : 
                row[k] = int(row[k])
            
        datas.append (row)
    
    last_row = sys.stdin.readline()
    
# print (datas)

# row check
for i in range (9) :
    seta = set()
        
    for j in range (9) :
        if datas[i][j] != 0 and datas[i][j] not in seta : 
            seta.add(datas[i][j])
            
        else : 
            if datas[i][j] != 0 : 
                print ('GRESKA')
                exit()
            
# col check 
for i in range (9) :
    seta = set()
    col = [datas[p][i] for p in range (9)]
    
    for j in range (9) :
        if col[j] != 0 and col[j] not in seta : 
            seta.add(col[j])
            
        else : 
            if col[j] != 0 : 
                print ('GRESKA')
                exit()

# box check
for i in range (0, 9, 3) : 
    for j in range (0, 9, 3) : 
        seta = set()
        box = [datas[i+p][j+k] for p in range (3) for k in range (3)]
        
        for k in range (9) :
            if box[k] != 0 and box[k] not in seta : 
                seta.add(box[k])
                
            else : 
                if box[k] != 0 : 
                    print ('GRESKA')
                    exit()
                    
print ('OK')

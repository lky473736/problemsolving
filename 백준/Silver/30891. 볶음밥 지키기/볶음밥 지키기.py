import sys

N, R = map(int, sys.stdin.readline().split())
position = []

mx, my = 0, 0
Mx, My = 0, 0

for i in range (N) :
    px, py = map(int, sys.stdin.readline().split())
    position.append ([px, py])
    
    if i == 0 :
        mx, Mx = px, px
        my, My = py, py
        continue
    
    if Mx < px : 
        Mx = px
        
    if My < py :
        My = py
        
    if mx > px : 
        mx = px
        
    if my > py : 
        my = py
        
# print (mx, Mx, my, My)
    
rice = []
    
for i in range (mx - R, Mx + R + 1) : 
    for j in range (my - R, My + R + 1) :
        counting = 0
        
        for compo in position : 
            if (i - compo[0])**2 + (j - compo[1])**2 <= R**2 :
                counting += 1 
            
        rice.append ([[i, j], counting])
    
# print (rice)
    
rice.sort (key = lambda x : (x[1]))
print (rice[-1][0][0], rice[-1][0][1])
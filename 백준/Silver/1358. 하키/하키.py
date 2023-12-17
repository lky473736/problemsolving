W, H, X, Y, P = map(int, input().split())

player = 0

for _ in range (P) : 
    px, py = map(int, input().split())
    
    if X <= px <= X + W and Y <= py <= Y + H :
        player += 1
        
    else :
        if pow(px-X, 2) + pow(py-Y-H//2, 2) <= pow(H//2, 2) : 
            player += 1
            
        elif pow(px-X-W, 2) + pow(py-Y-H//2, 2) <= pow(H//2, 2): 
            player += 1
            
        else :
            pass

print (player)
                
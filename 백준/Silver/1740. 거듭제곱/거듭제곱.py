# 참고 : https://m.blog.naver.com/js568/221979751444

N = int(input())

if N == 1 :
    print (1)
    exit()

bi = ""
tri = ""

a = N

while True : 
    b = a % 2
    a = a // 2
    bi = bi + str(b)
    
    if a == 1 : 
        bi = bi + str(a) 
        break

suma = 0
for i in range (len(bi)) :
    if int(bi[i]) == 1 : 
        suma += 3 ** i
        
print (suma)
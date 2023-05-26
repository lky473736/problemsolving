# fibonacci sequence

fibonacci = [1, 1] # 첫째 항과 둘째 항은 이미 들어가 있음

n = int(input("n? : ")) # 어디까지 계산할 건지 물음

for i in range (n - 2) : # 이미 첫째 항과 둘째 항이 있기 때문에 n - 2번 반복
    if i == 0 :
        pass
    
    elif i == 1 :
        pass
    
    k = fibonacci[i] + fibonacci[i + 1]
    fibonacci.append (k)
    
print (fibonacci)
print ("합은 : ", sum(fibonacci))

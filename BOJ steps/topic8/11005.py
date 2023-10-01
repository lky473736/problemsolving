# https://hymndev.tistory.com/17

N, B = map(int, input().split())

result = 0
numlist = []

number_to_alphabet = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L', 22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S', 29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

while True : 
    K = N % B
    N = N // B
    
    if N // B == N :
        numlist.append (K)
        break
    
    else :
        numlist.append (K)
        
for i in range (len(numlist)) :
    numlist[-1 - i] = number_to_alphabet[numlist[-1 - i]]

for j in range (len(numlist)) :
    print (numlist[-1 - j], end = '')

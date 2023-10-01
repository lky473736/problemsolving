string = input()
stringlist = []

for i in range (len(string)) :
    stringlist.append (string[i])

'''for j in stringlist : 
    if j.isupper() == True : 
        stringlist[stringlist.index(j)] = j.lower()
    
    else :
        stringlist[stringlist.index(j)] = j.upper()'''
        
# 대문자와 소문자 교차
for j in range(len(stringlist)):
    if stringlist[j].isupper():
        stringlist[j] = stringlist[j].lower()
        
    else:
        stringlist[j] = stringlist[j].upper()

for k in stringlist :
    print (k, end = '')

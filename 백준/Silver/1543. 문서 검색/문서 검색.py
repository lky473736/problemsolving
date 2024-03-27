import sys

doc = sys.stdin.readline().rstrip()
word = sys.stdin.readline().rstrip()

head = 0
length = len(word)
length_doc = len(doc)

counting = 0

while head < length_doc : 
    if doc[head:head+length] == word :
        counting += 1
        head = head + length
        
        continue
    
    head += 1
    
print (counting)
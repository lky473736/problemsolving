import sys

sentence = sys.stdin.readline().rstrip()
length = len(sentence)

answer = []
i = 0
mode = 0

compo_ans = ""

while True :
    if i == length : 
        break
    
    # print (sentence[i])
    
    if sentence[i] == 'W' :
        try : 
            if sentence[i:i+8] == "What is?" :
                answer.append (0)
                mode = 0
                i += 1
                continue
            
            if sentence[i:i+7] == "What is" :
                # print ("---------")
                i += 7
                mode = 1
                
        except : 
            pass
        
    else :
        if mode == 1 :
            if sentence[i] == '?' :
                mode = 0
                answer.append(compo_ans)
                compo_ans = ""
                
            else :
                if sentence[i] == '.' :
                    compo_ans = ""
                    mode = 0
                
                else :
                    compo_ans += sentence[i]
        
    i += 1
    
# print (answer)
    
for compo_ans in answer :
    if compo_ans != 0 :
        print (f'Forty-two is {compo_ans}.')
        
    else :
        print ('Forty-two is.')
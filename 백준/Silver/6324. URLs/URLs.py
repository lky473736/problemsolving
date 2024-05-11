'''
    port만 있고 path가 없는 경우가 반례같습니다.
'''

import sys

n = int(sys.stdin.readline())
URLS = []

for _ in range (n) :
    url = sys.stdin.readline().rstrip()
    URLS.append (url)

for it in range (n) :
    URL = URLS[it]
    URL += '*'
    
    colon = 0
    slash = 0
    token_colon = 0
    token_host = 0
    
    protocol = ""
    host = ""
    port = ""
    path = ""
    
    i = 0
    
    while URL[i] != '*' :
        if URL[i] == ':' :
            if colon == 0 : 
                protocol = URL[:i]
                
            elif slash == 2 and colon == 1 : 
                token_colon = i
                
            colon += 1
            
        if URL[i] == '/' : 
            if token_host > 0 or token_colon > 0 :
                token_host = 0
                
            if slash == 1 : 
                token_host = i+1
                
            elif slash == 2 :
                break
            
            slash += 1
            
        if URL[i] != '/' and URL[i] != ':' :
            if token_host > 0 :
                host += URL[i]
                
            elif token_host == 0 : 
                if token_colon > 0 :
                    port += URL[i]
        
        i += 1
        
    print (f"URL #{it+1}")
    
    if token_colon != 0 : # 토큰이 있을 때
        print ("Protocol =", protocol)
        print ("Host     =", host[:-1 * (i-token_colon)+1])
        print ("Port     =", URL[token_colon+1:i])
        
    else : # 토큰이 없을 때
        print ("Protocol =", protocol)
        print ("Host     =", host)
        print ("Port     = <default>")
        
    if URL[i+1:-1] == '' :
        print ("Path     = <default>")
            
    else :
        print ("Path     =", URL[i+1:-1])
        
    print ()
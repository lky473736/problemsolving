#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    std::string S;
    int joi = 0;
    int ioi = 0;
    
    std::cin >> S;
    
    for (int i = 0; i < S.length(); i++) {
        char c[4];
        
        for (int j = 0; j < 3; j++) {
            c[j] = S[i+j];
        }
        
        c[3] = '\0';
        
        if (strcmp(c, "JOI") == 0) {
            joi += 1;
        }
        
        else if (strcmp(c, "IOI") == 0) {
            ioi += 1;
        }
    }
    
    printf ("%d\n%d", joi, ioi);
    
    return 0;
}
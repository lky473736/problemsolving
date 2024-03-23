#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    char N[2017];
    int M = 0;
    int k = 0;
    
    scanf ("%s %d", N, &M);
    
    int intn = 0;
    
    if (strlen) {
        for (int i = 0; i < strlen(N); i++) {
            intn += pow(10, (strlen(N)-1-i)) * (int(N[i]) - 48);
        }
    }
    
    else {
        intn = int(N[0]);
    }
    
    // printf ("intn : %d\n / strlen : %d\n", intn, strlen(N));
    // printf ("%ld %d\n", strlen(N) * intn, M);
    
    if (strlen(N) * intn <= M) { 
        for (int i = 0; i < intn; i++) {
            for (int j = 0; j < strlen(N); j++) {
                printf ("%c", N[j]);
            }
        }
    }
    
    else {
        while (true) {
            int token = 0;
            
            for (int i = 0; i < strlen(N); i++) {
                if (k == M) {
                    token = 1;
                    break;
                }
                
                printf ("%c", N[i]);
                k++;
            }
            
            if (token == 1) {
                break;
            }
        }
    }
    
    return 0;
}
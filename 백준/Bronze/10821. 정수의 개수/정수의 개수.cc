#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    int num_comma = 0;
    char S[101];
    
    scanf ("%s", S);
    
    for (int i = 0; i < strlen(S); i++) {
        if (S[i] == ',') {
            num_comma++;
        }
    }
    
    printf ("%d", num_comma+1);
    
    return 0;
}
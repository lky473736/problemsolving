#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    int T; 
    scanf ("%d", &T);
    
    for (int i = 0; i < T; i++) {
        char string[1001];
        scanf ("%s", string);
        
        printf ("%c%c\n", string[0], string[strlen(string)-1]);
    }
    
    return 0;
}
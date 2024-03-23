#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    char s[101];
    scanf ("%s", s);
    
    int i = 0;
    int j = 0;
    
    char rst[100];
    
    while (true) {
        char c = s[i];
        
        if (c == '\0') {
            break;
        }
        
        if (65 <= (int)c && (int)c <= 90) {
            rst[j] = c;
            j++;
        }
        
        i++;
    }
    
    printf ("%s\n", rst);
    
    return 0;
}
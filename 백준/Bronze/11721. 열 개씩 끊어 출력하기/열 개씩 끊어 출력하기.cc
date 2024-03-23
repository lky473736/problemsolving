#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    char string[101];
    scanf ("%s", string);

    for (int i = 1; i <= strlen(string); i++) {
        printf ("%c", string[i-1]);
        
        if (i % 10 == 0) {
            printf ("\n");
        }
    }
    
    return 0;
}
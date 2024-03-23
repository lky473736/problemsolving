#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    int N;
    scanf ("%d", &N);

    for (int i = 0; i < N; i++) {
        char Si[21];
        scanf ("%s", Si);
        
        for (int j = 0; j < strlen(Si); j++) {
            printf ("%c", tolower(Si[j]));
        }
        
        printf ("\n");
    }
    
    return 0;
}
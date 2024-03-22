#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    while (true) {
        int M, F;
        scanf ("%d %d", &M, &F);
        
        if (M == F && M == 0) {
            break;
        }
        
        printf ("%d\n", M+F);
    }
    
    return 0;
}
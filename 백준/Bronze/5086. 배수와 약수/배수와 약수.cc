#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    while (true) {
        int A, B;
        scanf ("%d %d", &A, &B);
        
        if (A == B && A == 0) {
            break;
        }
        
        if (A % B == 0) {
            printf ("multiple\n");
        }
        
        else if (B % A == 0) {
            printf ("factor\n");
        }
        
        else {
            printf ("neither\n");
        }
    }
    
    return 0;
}
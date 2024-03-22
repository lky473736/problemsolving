#include <cstdio>
#include <iostream>

int main() {
    int T;
    scanf ("%d", &T);
    
    for (int i = 0; i < T; i++) {
        int p, q;
        scanf ("%d %d", &p, &q);
        
        printf ("Case %d: %d\n", i+1, p+q);
    }
    
    return 0;
}
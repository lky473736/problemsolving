#include <cstdio>
#include <iostream>

int main() {
    int S, T;
    int a, b, c, d;
    
    scanf ("%d %d %d %d", &a, &b, &c, &d);
    S += (a + b + c + d);
    scanf ("%d %d %d %d", &a, &b, &c, &d);
    T += (a + b + c + d);
    
    if (S < T) {
        printf ("%d\n", T);
    }
    
    else {
        printf ("%d\n", S);
    }
    
    return 0;
}
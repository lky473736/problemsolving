#include <cstdio>
#include <iostream>

int main() {
    int N;
    
    scanf ("%d", &N);
    
    // dp?
    if (N % 2 == 0) {
        printf ("CY\n");
    }
    
    else {
        printf ("SK\n");
    }
}
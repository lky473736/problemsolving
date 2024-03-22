#include <cstdio>
#include <iostream>

int main() {
    int N;
    static int winA, winB;
    
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++) {
        int A, B;
        scanf ("%d %d", &A, &B);
        
        if (A < B) {
            winB = winB + 1;
        }
        
        else if (A > B) {
            winA = winA + 1;
        }
    }
    
    printf ("%d %d\n", winA, winB);
}
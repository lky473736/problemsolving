#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    int N, K;
    scanf ("%d %d", &N, &K);
    
    int counting = 0;
    
    for (int i = 1; i <= N; i++) {
        if (N % i == 0) {
            counting += 1;
            
            if (counting == K) {
                printf ("%d\n", i);
                return 0;
            }
        }
    }
    
    printf ("0\n");
    
    return 0;
}
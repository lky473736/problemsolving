#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    int K, N, M;
    
    scanf ("%d %d %d", &K, &N, &M);
    
    if (K*N - M > 0) { 
        printf ("%d\n", K*N - M); 
    }
    
    else { 
        printf ("0\n"); 
        
    }
    
    return 0;
}
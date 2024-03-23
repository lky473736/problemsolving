#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    int A, I;
    int x = 0, K = 0;
    
    scanf ("%d %d", &A, &I);
    
    while (true) {
        K = int(x / A) + 1;
        
        if (K == I) {
            break;
        }
        
        x += 1;
    }
    
    printf ("%d\n", x+1);
	
	return 0;
}
#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    char chess[8][8];
    char str[9];
    
    for (int i = 0; i < 8; i++) {
        scanf("%s", str);
        
        for (int j = 0; j < 8; j++) {
            chess[i][j] = str[j];
        }
    }
    
    int white = 0;
    
    for (int i = 1; i <= 8; i++) {
        for (int j = 1; j <= 8; j++) {
            if (i % 2 == 0) { // row가 짝수일때
                if (j % 2 == 0 && chess[i-1][j-1] == 'F') {
                    white += 1;
                }
            }
            
            else {  // row가 홀수일 때
                if (j % 2 != 0 && chess[i-1][j-1] == 'F') {
                    white += 1;
                }
            }
        }
    }
    
    printf ("%d\n", white);
    
    return 0;
}
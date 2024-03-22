#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    int chess[] = {1, 1, 2, 2, 2, 8};
    int dh[6];
    
    scanf ("%d %d %d %d %d %d", dh, dh+1, dh+2, dh+3, dh+4, dh+5);
    
    for (int i = 0; i < 6; i++) {
        printf ("%d ", chess[i]-dh[i]);
    }
    
    return 0;
}


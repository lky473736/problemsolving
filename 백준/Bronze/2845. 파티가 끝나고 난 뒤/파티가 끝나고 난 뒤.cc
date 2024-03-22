#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    int L, P;
    scanf ("%d %d", &L, &P);
    
    int a, b, c, d, e;
    scanf ("%d %d %d %d %d", &a, &b, &c, &d, &e);
    
    printf ("%d %d %d %d %d\n", a-L*P, b-L*P, c-L*P, d-L*P, e-L*P);
    
    return 0;
}


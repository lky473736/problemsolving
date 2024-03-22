#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    int m = 0, d = 0;
    scanf ("%d %d", &m, &d);
    
    if (m == 2) {
        if (d < 18) {
            printf ("Before\n");
        }
        
        else if (d == 18) {
            printf ("Special\n");
        }
        
        else {
            printf ("After\n");
        }
    }
    
    else {
        if (m < 2) {
            printf ("Before\n");
        }
        
        else {
            printf ("After\n");
        }
    }
    
    return 0;
}
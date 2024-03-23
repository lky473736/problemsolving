#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    while (true) {
        int a, b;
        scanf ("%d %d", &a, &b);
        
        if (a == b && a == 0) {
            break;
        }
        
        if (a > b) {
            printf ("Yes\n");
        }
        
        else {
            printf ("No\n");
        }
    }
	
	return 0;
}
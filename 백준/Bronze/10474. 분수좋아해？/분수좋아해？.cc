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
        
        printf ("%d %d / %d\n", int(a/b), a - int(a/b)*b, b);
    }
	
	return 0;
}
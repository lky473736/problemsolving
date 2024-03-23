#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    int arr[5];
    
    for (int i = 0; i < 5; i++) {
        scanf ("%d", &arr[i]);
    }
    
    int X, Y;
    
    X = arr[0] * arr[4];
    
    if (arr[4] <= arr[2]) {
        Y = arr[1];
    }
    
    else {
        Y = arr[1] + (arr[4] - arr[2]) * arr[3];
    }
    
    if (X > Y) {
        printf ("%d\n", Y);
    }
    
    else {
        printf ("%d\n", X);
    }
	
	return 0;
}
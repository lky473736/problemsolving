#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    double arr[5] = {350.34, 230.90, 190.55, 125.30, 180.90};
    
    int T;
    scanf ("%d", &T);
    
    for (int i = 0; i < T; i++) {
        int number[5];
        scanf ("%d %d %d %d %d", number, number+1, number+2, number+3, number+4);
        
        double cost = 0.00;
        
        for (int j = 0; j < 5; j++) {
            cost += arr[j] * number[j];
        }
        
        printf ("$%.2lf\n", cost);
    }
    
    return 0;
}
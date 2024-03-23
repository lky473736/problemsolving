#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    double temp = 0;
    int counting = 0;
    
    while (true) {
        double a;
        scanf ("%lf", &a);
        
        if (int(a) == 999) {
            break;
        }
        
        if (counting == 0) {
            counting++;
            temp = a;
            continue;
        }
        
        printf ("%.2lf\n", a-temp);
        temp = a;
    }
    
    return 0;
}
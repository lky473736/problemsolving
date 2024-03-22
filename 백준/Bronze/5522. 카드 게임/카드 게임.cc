#include <cstdio>
#include <iostream>

int main() {
    int sum = 0;
    
    for (int i = 0; i < 5; i++) {
        int input = 0;
        scanf ("%d", &input);
        sum += input;
    }
    
    printf ("%d\n", sum);
    
    return 0;
}
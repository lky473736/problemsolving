#include <cstdio>
#include <iostream>

int main() {
    int sec[4];
    
    for (int i = 0; i < 4; i++) {
        int input;
        scanf ("%d", &input);
        
        sec[i] = input;
    }
    
    int suma = 0;
    
    for (int i = 0; i < 4; i++) {
        suma += sec[i];
    }
    
    printf ("%d\n", int(suma / 60));
    printf ("%d", suma % 60);
    
    return 0;
}
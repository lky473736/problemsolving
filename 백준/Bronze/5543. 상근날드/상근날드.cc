#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    int arr[5];
    
    for (int i = 0; i < 5; i++) {
        int compo = 0;
        scanf ("%d", &compo);
        
        arr[i] = compo;
    }
    
    int suma = 0;
    int mina = arr[0];
    
    for (int i = 0; i < 3; i++) {
        if (mina > arr[i]) {
            mina = arr[i];
        }
    }
    
    suma += mina;
    mina = arr[3];
    
    for (int i = 3; i < 5; i++) {
        if (mina > arr[i]) {
            mina = arr[i];
        }
    }
    
    suma += mina;
    
    printf ("%d\n", suma-50);
    
    return 0;
}
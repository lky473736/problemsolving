#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    while (true) {
        int i, j, k;
        scanf ("%d %d %d", &i, &j, &k);
        
        if (i == j && j == k && i == 0) {
            break;
        }
        
        int arr[] = {i, j, k};
        int size = sizeof(arr) / sizeof(*arr);
        
        int max = *std::max_element(arr, arr + size);
        int ind;
        
        // find index of max
        for (int l = 0; l < 3; l++) {
            if (max == arr[l]) {
                ind = l;
                break;
            }
        }
        
        int suma = 0;
        for (int l = 0; l < 3; l++) {
            if (ind == l) {
                continue;
            }
            
            suma += arr[l];
        }
        
        // printf ("%d %d\n", suma, max);
        
        if (suma <= max) {
            printf ("Invalid\n");
            continue;
        }
        
        if (i == j && j == k) {
            printf ("Equilateral\n");
        }
        
        else if (i == j || j == k || i == k) {
            printf ("Isosceles\n");
        }
        
        else if (i != j && j != k) {
            printf ("Scalene\n");
        }
    }
    
    return 0;
}

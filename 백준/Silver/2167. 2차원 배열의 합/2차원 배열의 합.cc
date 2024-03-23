#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    int N, M; 
    scanf ("%d %d", &N, &M);
    
    int** arr = new int*[N];
    
    for (int i = 0; i < N; i++) {
        arr[i] = new int[M];
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int input;
            std::cin >> input;
            arr[i][j] = input;
        }
    }
    
    // for (int i = 0; i < N; i++) {
    //     for (int j = 0; j < M; j++) {
    //         printf ("%d ", arr[i][j]);
    //     }
    //     printf ("\n");
    // }
    
    int K;
    scanf ("%d", &K);
    
    for (int l = 0; l < K; l++) {
        int i, j, x, y;
        scanf ("%d %d %d %d", &i, &j, &x, &y);
        
        int suma = 0;
        
        for (int v = i-1; v <= x-1; v++) {
            for (int c = j-1; c <= y-1; c++) {
                suma += arr[v][c];
            }
        }
        
        printf ("%d\n", suma);
    }
    
    return 0;
}
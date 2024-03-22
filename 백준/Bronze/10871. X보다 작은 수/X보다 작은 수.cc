#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    int N, X;
    scanf ("%d %d", &N, &X);
    
    int *arr = new int[N];
    
    for (int i = 0; i < N; i++) {
        scanf ("%d", arr+i);
    }
    
    for (int i = 0; i < N; i++) {
        if (arr[i] < X) {
            std::cout << arr[i] << ' ';
        }
    }
    
    return 0;
}
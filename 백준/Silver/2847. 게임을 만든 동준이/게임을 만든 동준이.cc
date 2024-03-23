#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>

int main() {
    int N;
    scanf ("%d", &N);
    
    int *arr = new int[N];
    
    for (int i = 0; i < N; i++) {
        int input;
        std::cin >> input;
        arr[i] = input;
    }
    
    int w = 0;
    
    for (int i = 1; i < N; i++) {
        if (arr[N-1-i] >= arr[N-i]) {
            w += abs(arr[N-i] - arr[N-1-i]) + 1;
            arr[N-1-i] = arr[N-i] - 1;
        }
    }
    
    printf ("%d\n", w);
	
	return 0;
}
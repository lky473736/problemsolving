#include <bits/stdc++.h>
#include <time.h>
using namespace std;

int binary_search (int n, int* arr, int x) {
    int mid = 0, start = 0, end = n-1;
    
    while (start <= end) {
        mid = (start + end) / 2;
        if (arr[mid] == x) { return mid; }
        else if (arr[mid] > x) { end = mid - 1;}
        else { start = mid + 1;}
    }
    return 0;
}

int sequential_search (int n, int* arr, int x) {
    int ind = 0;
    while (ind <= n && arr[ind] != x) {
        ind++;
    } 
    if (ind > n) {
        return 0;
    }
    return ind;
}

int main() {
    clock_t start, end;
    
    int arr[100000];
    for (int i = 0; i < 1024; i++) {
        arr[i] = i+1;
    }
    
    int n;
    cout << "input n that is scale of 1 to 100000 : ";
    cin >> n;
    
    start = clock();
    binary_search (1024, arr, n);
    end = clock();
    double result = (double)(end-start);
    cout << "binary : " << result << "ns" << endl;
    
    start = clock();
    sequential_search (1024, arr, n);
    end = clock();
    result = (double)(end-start);
    cout << "sequential : " << result << "ns" << endl;
}

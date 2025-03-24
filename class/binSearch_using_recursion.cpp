#include <bits/stdc++.h>
#include <time.h>
using namespace std;

// binary searching using recursion (divide and conquer)

int bin_recur (int low, int high, int x, int *arr) {
    if (low > high) return -1;
    
    int mid = (low + high) / 2;
    
    if (arr[mid] == x) return mid;
    if (arr[mid] > x) return bin_recur(low, mid-1, x, arr);
    if (arr[mid] < x) return bin_recur(mid+1, high, x, arr); 
}

int main() {
    clock_t start, end;
    
    int arr[1024];
    for (int i = 0; i < 1024; i++) {
        arr[i] = i+1;
    }
    
    int n;
    cout << "input n that is scale of 1 to 1024 : ";
    cin >> n;
    
    start = clock();
    int ind = bin_recur (0, 1023, n, arr);
    end = clock();
    
    double result = (double)(end-start);
    
    cout << "index : " << ind + 1 << endl; // if 0, there isn't element 
    cout << "binary : " << result << "ns" << endl;
}
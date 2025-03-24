#include <bits/stdc++.h>
#include <time.h>
using namespace std;

int recursive_fib (int n) {
    if (n <= 1) {
        return n;
    } 
    else {
        return recursive_fib(n-1) + recursive_fib(n-2);
    }
}

int iterative_fib (int n) {
    int *arr = new int[n+1];
    arr[0] = 0; arr[1] = 1;
    if (n < 1) {
        return 0;
    }
    else {
        for (int i = 2; i <= n; i++) {
            arr[i] = arr[i-1] + arr[i-2];
        }
    }
    return arr[n];
}

int main() {
    clock_t start, end;
    
    int n;
    cout << "input n that is scale of 1 to 100000 : ";
    cin >> n;
    
    start = clock();
    int k1 = recursive_fib(n);
    end = clock();
    double result = (double)(end-start);
    cout << "rst : " << k1 << endl;
    cout << "recursive : " << result << "ns" << endl;
    
    start = clock();
    int k2 = iterative_fib(n);
    end = clock();
    result = (double)(end-start);
    cout << "rst : " << k2 << endl;
    cout << "iterative : " << result << "ns" << endl;
}

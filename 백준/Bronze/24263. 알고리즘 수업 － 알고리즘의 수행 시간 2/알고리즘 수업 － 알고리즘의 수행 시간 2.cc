#include <bits/stdc++.h>
using namespace std;

int MenOfPassion(int *A, int n) {
    int sum = 0;
    int k = 0;
    for (int i = 0; i < n; i++) {
        sum = sum + A[i];
        k++;
    }
    return k;
}

int main() {
    int n; cin >> n;
    int arr[n];
    int k = MenOfPassion(arr, n);
    cout << k << '\n' << 1;
}
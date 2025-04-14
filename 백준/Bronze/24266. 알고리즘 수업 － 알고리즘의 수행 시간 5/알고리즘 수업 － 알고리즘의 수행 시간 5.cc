#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll MenOfPassion(int *A, int n) {
    int sum = 0;
    ll p = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            for (int k = 0; k < n; k++) {
                // sum += A[i] × A[j] × A[k];
                p++;
            }
        }
    }
    return p;
}

int main() {
    ll n; cin >> n;
    // int arr[n];
    // ll k = MenOfPassion(arr, n);
    ll k = n * n * n;
    // for (ll i = n-1; i > 0; i--) { k += i; }
    cout << k << '\n' << 3;
}
#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll MenOfPassion(int *A, int n) {
    ll sum = 0, k = 0;
    for (int i = 0; i < n-1; i++) {
        for (int j = i + 1; j < n; j++) {
            sum += A[i] * A[j]; 
            k++;
        }
    }
    return k;
}

// 7
// step 1 : i = 0 j = 1, 2, 3, 4, 5, 6 
// step 2 : i = 1 j = 2, 3, 4, 5, 6
// step 3 : i = 2 j = 3, 4, 5, 6
// step 4 : i = 3 j = 4, 5, 6
// step 5 : i = 4 j = 5, 6
// step 6 : i = 5 j = 6

int main() {
    int n; cin >> n;
    int arr[n];
    // ll k = MenOfPassion(arr, n);
    ll k = 0;
    for (ll i = n-1; i > 0; i--) { k += i; }
    cout << k << '\n' << 2;
}
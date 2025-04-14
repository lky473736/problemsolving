#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

// ll MenOfPassion(int *A, int n) {
//     int sum = 0;
//     ll k = 0;
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             sum += A[i] * A[j];
//             k++;
//         }
//     }
//     return k;
// }

int main() {
    int n; cin >> n;
    // int arr[n];
    // ll k = MenOfPassion(arr, n);
    long long k = pow(n, 2);
    cout << k << '\n' << 2;
}
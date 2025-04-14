#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

ll MenOfPassion(ll *A, ll n) {
    ll sum = 0, p = 0;
    for (int i = 0; i < n-2; i++) {
        for (int j = i+1; j < n-1; j++) {
            for (int k = j+1; k < n; k++) {
                //  sum <- sum + A[i] × A[j] × A[k]; # 코드1
                p++;
            }
        }
    }
    return p;
}

// 7
// i = 1 j = 2 ~ 6 k = 3 ~ 7 -> 5 * 5 = 25
// i = 2 j = 3 ~ 6 k = 4 ~ 7 -> 4 * 4 = 16
// i = 3 j = 4 ~ 6 k = 5 ~ 7 -> 3 * 3 = 9
// i = 4 j = 5 ~ 6 k = 6 ~ 7 -> 2 * 2 = 4
// i = 5 j = 6 ~ 6 k = 7 ~ 7 -> 1 * 1 = 1
// 20
// 12
// 6
// 2
// 1

int main() {
    ll n; cin >> n;
    // ll arr[n];
    // ll k = MenOfPassion(arr, n);
    // ll k = n * n * n;
    // for (ll i = n-1; i > 0; i--) { k += i; }
    ll k = 0;
    for (ll i = 1; i < n; i += 2) {
        k += (n-i-1) * (n-i-1);
    }
    cout << k << '\n' << 3;
}
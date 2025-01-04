#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);

    ll a, b; cin >> a >> b;
    if (a == b) {
        cout << 0 << '\n';
        goto k;
    }
    else if (a > b) {
        swap(a, b); 
    }
    
    cout << b - a - 1 << '\n';
k:
    for (ll i = a+1; i <= b-1; i++) cout << i << ' ';    
}
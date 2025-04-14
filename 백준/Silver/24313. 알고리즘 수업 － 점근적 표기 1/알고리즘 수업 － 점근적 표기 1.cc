#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main(void) {
    int a1, a0; cin >> a1 >> a0;
    int c; cin >> c;
    int n0; cin >> n0;
    
    if (a1 <= c && a1 * n0 + a0 <= c * n0 && a1 * (n0+1) + a0 <= c * (n0+1)) {
        cout << '1';
    }
    else {
        cout << '0';
    }
}
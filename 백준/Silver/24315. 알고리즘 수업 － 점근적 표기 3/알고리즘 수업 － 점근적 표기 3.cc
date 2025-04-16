#include <bits/stdc++.h>
using namespace std;

int main() {
    int a1, a0; cin >> a1 >> a0;
    int c1, c2; cin >> c1 >> c2;
    int n0; cin >> n0;
    
    if (c1 <= a1 and c2 >= a1) {
        if (c1*n0 <= a1*n0 + a0 and a1*n0 + a0 <= c2*n0) {
            cout << 1;
            return 0;
        }
        else {
            ;
        }
    }
    
    cout << 0;
}
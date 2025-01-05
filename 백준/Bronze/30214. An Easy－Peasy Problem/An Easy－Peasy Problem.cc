#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    int a, b; cin >> a >> b;
    
    if (b <= a*2) cout << "E";
    else cout << "H";

    return 0;
}
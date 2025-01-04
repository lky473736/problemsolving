#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);

    int a1, a2, a3;
    cin >> a1 >> a2 >> a3;

    if (a1 == a2 && a2 == a3) {
        cout << 10000 + a1 * 1000;
    }
    else {
        if (a1 == a2 && a2 != a3) {
            cout << 1000 + a1 * 100;
        }
        else if (a1 == a3 && a3 != a2) {
            cout << 1000 + a1 * 100;
        }
        else if (a2 == a3 && a1 != a3) {
            cout << 1000 + a2 * 100;
        }
        else {
            int max = (a1 > a2) ? ((a1 > a3) ? a1 : a3) : ((a2 > a3) ? a2 : a3); 
            cout << 100 * max;
        }
    }

    return 0;
}
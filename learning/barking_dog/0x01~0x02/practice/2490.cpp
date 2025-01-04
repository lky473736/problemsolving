#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);

    for (int i = 0; i < 3; i++) {
        int cnt_0 = 0; 
        for (int j = 0; j < 4; j++) {
            int compo;
            cin >> compo;
            if (compo == 0) cnt_0++;
        }

        if (cnt_0 == 0) cout << 'E';
        if (cnt_0 == 1) cout << 'A';
        if (cnt_0 == 2) cout << 'B';
        if (cnt_0 == 3) cout << 'C';
        if (cnt_0 == 4) cout << 'D';
        cout << '\n';
    }
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);

    int min = 0;
    int sum = 0;
    int cnt = 0;

    for (int i = 0; i < 7; i++) {
        int compo; cin >> compo;
        if (compo % 2 != 0) {
            if (cnt == 0) 
                min = compo;
            else 
                if (min > compo) min = compo;
            sum += compo;
            cnt++;
        }
    }
    if (cnt != 0) cout << sum << '\n' << min;
    else cout << -1;
    return 0;
}
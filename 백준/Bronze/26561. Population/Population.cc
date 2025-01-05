#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int N; cin >> N;
    for (int i = 0; i < N; i++) {
        ll a, b; cin >> a >> b;
        // for (int j = 1; j <= b; j++) {
        //     if (j % 4 == 0) {
        //         a++;
        //     }
        //     if (j % 7 == 0) {
        //         a--;
        //     }
        // }
        ll births = b / 4;
        ll deaths = b / 7;
        a = a + births - deaths;
        cout << a << '\n';
    }

    return 0;
}
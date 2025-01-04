#include <bits/stdc++.h>
using namespace std;
// typedef long long ll;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int max = 0, posi = 0;
    int compo;
    for (int i = 0; i < 9; i++) {
        cin >> compo;
        if (i == 0) { max = compo; posi = i; }
        if (compo > max) { max = compo; posi = i; }
    }
    cout << max << '\n' << posi+1;
    return 0;
}
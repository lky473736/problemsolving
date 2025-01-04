#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int N, X;
    cin >> N >> X;
    int compo;
    
    for (int i = 0; i < N; i++) {
        cin >> compo;
        if (compo < X) cout << compo << ' ';
    }
    
    return 0;
}
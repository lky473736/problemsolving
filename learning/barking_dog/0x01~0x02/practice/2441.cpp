#include <bits/stdc++.h>
using namespace std;
// typedef long long ll;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int N; cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < i; j++) {
            cout << ' ';
        }
        for (int j = 0; j < N-i; j++) {
            cout << '*';
        }
        cout << '\n';
    }

    return 0;
}
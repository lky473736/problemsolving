#include <bits/stdc++.h>
using namespace std;
// typedef long long ll;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int N; cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < i+1; j++) {
            cout << '*';
        }
        for (int j = 0; j < 2*N-i*2-2; j++) {
            cout << ' ';
        }
        for (int j = 0; j < i+1; j++) {
            cout << '*';
        }
        cout << '\n';
    }
    for (int i = 0; i < N-1; i++) {
        for (int j = 0; j < N-1-i; j++) {
            cout << '*';
        }
        for (int j = 0; j < 2*i+2; j++) {
            cout << ' ';
        }
        for (int j = 0; j < N-1-i; j++) {
            cout << '*';
        }
        cout << '\n';
    }

    return 0;
}
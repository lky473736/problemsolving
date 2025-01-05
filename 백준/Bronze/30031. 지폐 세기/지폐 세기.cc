#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int N; cin >> N;
    int sum = 0;
    
    for (int i = 0; i < N; i++) {
        int a, b; cin >> a >> b;
        if (a == 136) sum += 1000;
        if (a == 142) sum += 5000;
        if (a == 148) sum += 10000;
        if (a == 154) sum += 50000;
    }
    
    cout << sum;

    return 0;
}
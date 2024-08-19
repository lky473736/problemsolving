#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    
    int sangsa[100003] = {0}; // 상사
    int ching_chan[100003] = {0}; // 칭찬
    
    int garbage;
    cin >> garbage;
    
    for (int i = 1; i < n; i++) { 
        cin >> sangsa[i]; // -1, 1, 2, 3, 4 (이거 상사)
    }
    
    for (int j = 0; j < m; j++) {
        int i, w;
        cin >> i >> w; // 3, 3
        ching_chan[i] += w; // i에게 w만큼 (0, 0, 2, 4, 6, 0, 0, ...)
    }
    
    for (int i = 1; i < n+1; i++) {
        ching_chan[i] += ching_chan[sangsa[i-1]]; // 상사의 칭찬을 부하직원에게 줌
    }

    for (int i = 1; i < n+1; i++) {
        cout << ching_chan[i] << ' ';
    }
    
    return 0;
}
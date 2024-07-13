#include <bits/stdc++.h>
using namespace std;

int recu (int N, int r, int c) {
    if (N == 0) {
        return 0;
    }
    
    else {
        int recurnum = 2*(r % 2) + c % 2;
        
        return 4 * recu (N - 1, r/2, c/2) + recurnum;
    }
    
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N, r, c;
    cin >> N >> r >> c;
    
    cout << recu(N, r, c);
    
    return 0;
}
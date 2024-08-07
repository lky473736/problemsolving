#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    int N, M;
    cin >> N >> M;
    
    unordered_map<string, string> db;
    
    for (int i = 0; i < N; i++) {
        string site, pw;
        cin >> site >> pw;
        
        db[site] = pw;
    }
    
    for (int i = 0; i < M; i++) {
        string target;
        cin >> target;
        
        cout << db[target] << '\n';
    }
    
    return 0;
}

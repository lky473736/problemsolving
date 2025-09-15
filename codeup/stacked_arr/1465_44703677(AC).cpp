#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    int m; cin >> m;
    int num;
    
    vector<vector<int>> v(n, vector<int>(m));
    num = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            v[i][j] = num++;
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << v[n-i-1][j] << ' ';
        }
        cout << '\n';
    }
    
    return 0;   
}

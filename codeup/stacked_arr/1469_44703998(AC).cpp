#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    int m = n;
    int num = 1;
    
    vector<vector<int>> v(n, vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            v[i][j] = num++;
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (i % 2 != 0) {
            for (int j = 0; j < m; j++) {
                cout << v[i][j] << ' ';
            }
        } else {
            for (int j = m-1; j >= 0; j--) {
                cout << v[i][j] << ' ';
            }
        }
        cout << '\n';
    }
    
    return 0;   
}

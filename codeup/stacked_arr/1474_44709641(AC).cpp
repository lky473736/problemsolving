#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    int m; cin >> m;
    int num = n*m;
    
    vector<vector<int>> v(n, vector<int>(m));
    int token = m;
    
    for (int i = 0; i < m; i++) {
        if (token-- % 2 == 0) {
            num -= n-1;
            for (int j = 0; j < n; j++) {
                v[j][i] = num++;
            }
            num -= n+1;
        }
        else {
            for (int j = 0; j < n; j++) {
                v[j][i] = num--;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << v[i][j] << ' ';
        }
        cout << '\n';
    }
    
    return 0;   
}

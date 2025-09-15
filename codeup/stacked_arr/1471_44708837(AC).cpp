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
        if (i % 2 != 0) {
            for (int j = 0; j < m; j++) {
                v[j][i] = num++;
            }
        } else {
            num += n-1;
            for (int j = 0; j < m; j++) {
                v[j][i] = num--;
            }
            num += n+1;
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

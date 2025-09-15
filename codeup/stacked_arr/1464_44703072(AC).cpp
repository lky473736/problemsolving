#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    int m; cin >> m;
    int num;
    for (int i = 0; i < n; i++) {
        num = (n-i) * m;
        for (int j = 0; j < m; j++) {
            cout << num-- << ' ';
        }
        cout << '\n';
    }
    
    return 0;   
}

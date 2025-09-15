#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n; cin >> n;
    int num;
    for (int i = 0; i < n; i++) {
        num = i+1;
        for (int j = 0; j < n; j++) {
            cout << num << ' '; 
            num += n;
        }
        cout << '\n';
    }
    
    return 0;   
}

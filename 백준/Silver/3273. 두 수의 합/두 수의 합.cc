#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    int arr[100001] = {};
    bool appear[2000001];
    
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    sort(arr, arr+n);
    
    int x;
    cin >> x;
    
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (x-arr[i] > 0 && appear[x-arr[i]] == true) { 
            cnt++;
        }

        appear[arr[i]] = true;
    }

    cout << cnt;
    
    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int max_crt = arr[0];
    int max_gl = arr[0];
    
    for (int i = 1; i < n; ++i) {
        max_crt = max(arr[i], max_crt + arr[i]);
        if (max_crt > max_gl) {
            max_gl = max_crt;
        }
    }

    cout << max_gl;
    return 0;
}

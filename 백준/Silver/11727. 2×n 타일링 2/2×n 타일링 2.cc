#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    long long arr[1002] = {1, 1};
    
    for (int i = 2; i <= n; i++) {
        arr[i] = (arr[i-2] * 2 + arr[i-1]) % 10007;
    }
    
    cout << (arr[n]) ;
    
    return 0;
}

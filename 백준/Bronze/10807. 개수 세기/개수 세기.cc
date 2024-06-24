#include <bits/stdc++.h>
using namespace std;

int main() {
    int N = 0;
    cin >> N;
    
    int *arr = new int[N]();
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }
    
    int v = 0;
    cin >> v;
    
    int cnt = 0;
    for (int i = 0; i < N; i++) {
        if (arr[i] == v) {
            cnt++;
        }
    }
    
    cout << cnt;
    
    return 0;
}
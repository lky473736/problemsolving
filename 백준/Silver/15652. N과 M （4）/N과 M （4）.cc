#include <bits/stdc++.h>
using namespace std;

vector<int> arr;

void func (int prev, int cnt, int n, int m) {
    if (cnt == m) {
        for (int i = 0; i < m; i++) {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        
        return;
    }
    
    for (int i = prev; i <= n; i++) {
        arr.push_back(i);
        func (i, cnt + 1, n, m);
        arr.pop_back(); // 배열 상태 복원
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    
    func (1, 0, n, m);
    
    return 0;
}
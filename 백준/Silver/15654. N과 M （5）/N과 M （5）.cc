#include <bits/stdc++.h>
using namespace std;

vector<int> arr;  
vector<int> nums; 
bool visited[8];  

void func(int cnt, int n, int m) {
    if (cnt == m) {
        for (int i = 0; i < m; i++) {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            arr.push_back(nums[i]);
            func(cnt + 1, n, m);
            arr.pop_back(); // 백트래킹을 위해 추가한 수 제거
            visited[i] = false;
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    
    nums.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end()); // 사전 순으로 출력하기 위해 정렬
    
    func(0, n, m);
    
    return 0;
}

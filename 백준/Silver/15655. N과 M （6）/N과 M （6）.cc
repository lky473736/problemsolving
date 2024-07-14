#include <bits/stdc++.h>
using namespace std;

vector<int> arr; 
vector<int> nums;
bool visited[8];  

void func(int start, int cnt, int n, int m) {
    if (cnt == m) {
        for (int i = 0; i < m; i++) {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for (int i = start; i < n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            arr.push_back(nums[i]);
            func(i + 1, cnt + 1, n, m);
            arr.pop_back(); 
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
    
    func(0, 0, n, m); 
    
    return 0;
}

#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> arr;
vector<int> nums;
vector<int> check;
set<vector<int>> total;

void func(int cnt) {
    if (cnt == m) {
        total.insert(arr);
        return;
    }

    for (int i = 0; i < n; ++i) {
        // if (!check[i]) {
        //     check[i] = 1;
        arr.push_back(nums[i]);
        func(cnt + 1);
        arr.pop_back();
        //     check[i] = 0;
        // }
    }
}

int main() {
    cin >> n >> m;
    
    nums.resize(n);
    check.resize(n);
    
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    
    sort(nums.begin(), nums.end());
    
    func(0);
    
    for (const auto& seq : total) {
        for (int i = 0; i < m; ++i) {
            cout << seq[i] << ' ';
        }
        cout << '\n';
    }
    
    return 0;
}
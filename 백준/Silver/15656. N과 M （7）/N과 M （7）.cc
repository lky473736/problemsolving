#include <bits/stdc++.h>
using namespace std;

vector<int> arr;  
vector<int> nums; 

void func(int cnt, int n, int m) {
    if (cnt == m) {
        for (int i = 0; i < m; i++) {
            cout << arr[i] << ' ';
        }
        cout << '\n';
        return;
    }

    for (int i = 0; i < n; i++) {
        arr.push_back(nums[i]);
        func(cnt + 1, n, m);
        arr.pop_back(); 
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    
    nums.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end()); 
    
    func(0, n, m); 
    
    return 0;
}

#include <bits/stdc++.h>
using namespace std;

int n, m;
int arr[10];
int nums[10];
// set<vector<int>> total;

void func(int cnt, int start) {
    if (cnt == m) {
        for (int i = 0; i < m; i++) {
            cout << arr[i] << ' ';
        }
        
        cout << '\n';
        return;
    }

    int prev = 0;
    for (int i = start; i < n; i++) {
        if (prev != nums[i]) {
            arr[cnt] = nums[i];
            prev = arr[cnt];
            func(cnt+1, i+1); 
            // arr.pop_back();
        }
    }
}

int main() {
    cin >> n >> m;
    
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    sort(nums, nums + n);
    
    func(0, 0);
    
    return 0;
}
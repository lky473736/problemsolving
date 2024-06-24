#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[3];
    string rst = "";
    
    for (int i = 0; i < 3; i++) {
        cin >> arr[i];
    }
    
    rst = to_string(arr[0] * arr[1] * arr[2]);
    
    int appear[10] = {};
    for (char c : rst) {
        appear[int(c) - 48] += 1;
    }
    
    for (int z : appear) {
        cout << z << '\n';
    }
    
    return 0;
}
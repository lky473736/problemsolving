#include <bits/stdc++.h>
using namespace std;

int main() {
    string S;
    cin >> S;
    
    int arr[26];
    memset(arr, 0, sizeof(arr));
    
    for (int i = 0; i < S.size(); i++) {
        if (97 <= int(S[i]) && int(S[i]) <= 122) {
            arr[int(S[i]) - 97] += 1;
        }
    }
    
    for (int i = 0; i < 26; i++) {
        cout << arr[i] << ' ';
    }
    
    return 0;
}
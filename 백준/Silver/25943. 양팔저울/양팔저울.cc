#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[10000];
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long weights[2] = {arr[0], arr[1]};

    for (int i = 2; i < n; i++) {
        if (weights[0] == weights[1]) {
            weights[0] += arr[i];
        } 
        
        else {
            if (weights[0] < weights[1]) {
                weights[0] += arr[i];
            } 
            
            else {
                weights[1] += arr[i];
            }
        }
    }

    long long difference = abs(weights[0] - weights[1]);
    int cnt = 0;

    // cout << difference << '\n';

    int nums[] = {100, 50, 20, 10, 5, 2, 1};
    for (auto num : nums) {
        if (difference == 0) {
            break;
        }

        cnt += difference / num;
        difference %= num;
    }

    cout << cnt;

    return 0;
}
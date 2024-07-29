#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> dp(N + 1, N); 
    dp[0] = 0;  // 0을 표현하는 방법 : 0개

    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j * j <= i; ++j) {
            dp[i] = min(dp[i], dp[i - j * j] + 1);
        }
    }

    cout << dp[N];

    return 0;
}

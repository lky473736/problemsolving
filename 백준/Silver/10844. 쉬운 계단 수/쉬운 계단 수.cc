#include <iostream>
using namespace std;

int main() {
    int N;
    cin >> N;

    int dp[101][10] = {0};

    for (int i = 1; i <= 9; ++i) {
        dp[1][i] = 1;
    }

    for (int i = 2; i <= N; ++i) {
        for (int j = 0; j <= 9; ++j) {
            if (j > 0) {
                dp[i][j] += dp[i-1][j-1];
            }
            
            if (j < 9) {
                dp[i][j] += dp[i-1][j+1];
            }
            
            dp[i][j] %= 1000000000;
        }
    }

    int rst = 0;
    for (int j = 0; j <= 9; ++j) {
        rst += dp[N][j];
        rst %= 1000000000;
    }

    cout << rst;
    return 0;
}

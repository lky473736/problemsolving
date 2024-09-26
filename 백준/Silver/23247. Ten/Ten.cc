#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int m, n;
    cin >> m >> n;

    vector<vector<int>> land(m, vector<int>(n)); // 땅
    vector<vector<int>> prefix(m + 1, vector<int>(n + 1, 0)); // 누적합

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> land[i][j]; // 땅입력받기
            prefix[i + 1][j + 1] = land[i][j] + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j];
        }
    }

    int cnt = 0;

    for (int row_1 = 1; row_1 <= m; row_1++) {
        for (int col_1 = 1; col_1 <= n; col_1++) {
            for (int row_2 = row_1; row_2 <= m; row_2++) {
                for (int col_2 = col_1; col_2 <= n; col_2++) {
                    int sum = prefix[row_2][col_2] - prefix[row_1 - 1][col_2] - prefix[row_2][col_1 - 1] + prefix[row_1 - 1][col_1 - 1];
                    
                    if (sum == 10) {
                        cnt++;
                    }
                    
                    if (sum > 10) {
                        break;
                    }
                }
            }
        }
    }

    cout << cnt << '\n';
    return 0;
}

#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int N;
        cin >> N;
        vector<int> list_coin(N);

        for (int i = 0; i < N; ++i) {
            cin >> list_coin[i];
        }

        int M;
        cin >> M;
        vector<int> counting(M + 1, 0);

        for (int coin : list_coin) {
            if (coin > M) {
                continue;
            }

            counting[coin] += 1;

            for (int i = coin + 1; i <= M; ++i) {
                counting[i] += counting[i - coin];
            }
        }

        cout << counting[M] << '\n';
    }

    return 0;
}

#include <bits/stdc++.h>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;

    vector<bool> is_prime(N + 1, true);
    int cnt = 0;
    int rst = -1;

    for (int p = 2; p <= N; ++p) {
        if (is_prime[p]) {
            for (int multiple = p; multiple <= N; multiple += p) {
                if (is_prime[multiple]) {
                    is_prime[multiple] = false;
                    cnt++;
                    
                    if (cnt == K) {
                        rst = multiple;
                        break;
                    }
                }
            }
            
            if (rst != -1) {
                break;
            }
        }
    }

    cout << rst << '\n';

    return 0;
}

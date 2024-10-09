#include <bits/stdc++.h>
using namespace std;

const long long MOD = 16769023;

// 거듭제곱 모듈러 연산 함수
long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    long long n;
    cin >> n;

    if (n % 2 == 0) {
        cout << mod_pow(2, n / 2, MOD);
    } else {
        cout << mod_pow(2, (n + 1) / 2, MOD);
    }

    return 0;
}

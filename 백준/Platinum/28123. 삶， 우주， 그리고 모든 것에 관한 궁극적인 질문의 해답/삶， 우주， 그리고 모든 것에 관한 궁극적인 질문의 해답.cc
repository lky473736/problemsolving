#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N, K, X;
    cin >> N >> K >> X;

    cout << N - 3 * (K - 1) - ((long long)ceil(sqrt((long double)X)) - 1) << "\n";

    return 0;
}

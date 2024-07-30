#include <bits/stdc++.h>
using namespace std;

// 그냥 조합 구하고 2랑 5 소인수분해했을 때 최소 쌍 구하면 될듯
// 분자가 가진 5갯수 - 분모가 가진 5갯수
// 분자가 가진 2갯수 - 분모가 가진 2갯수
// 둘 중 최소

#include <bits/stdc++.h>
using namespace std;

long long cnt_factors (long long n, int factor) {
    long long cnt = 0;
    
    while (n) {
        n /= factor;
        cnt += n;
    }
    
    return cnt;
}

int main() {
    long long n, m;
    cin >> n >> m;

    long long cnt_2 = cnt_factors(n, 2) - cnt_factors(n - m, 2) - cnt_factors(m, 2);
    long long cnt_5 = cnt_factors(n, 5) - cnt_factors(n - m, 5) - cnt_factors(m, 5);
    
    cout << min(cnt_2, cnt_5) << '\n';

    return 0;
}
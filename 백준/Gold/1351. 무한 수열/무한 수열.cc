// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     cin.tie(NULL);
//     ios::sync_with_stdio(false);
    
//     long long N, P, Q;
//     cin >> N >> P >> Q;
    
//     unordered_map<long long, long long> mapping;
//     mapping[0] = 1;
//     // long long rst = 0;
    
//     for (auto i = 1; i <= N; i++) {
//         mapping[i] = mapping[floor(i / P)] + mapping[floor(i / Q)];
//         // cout << mapping[i] << floor(i/P) << floor(i/Q) << endl;
//     }
    
//     cout << mapping[N] << '\n';
    
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

unordered_map<long long, long long> mapping;

long long DP (long long i, long long P, long long Q) {
    if (mapping.find(i) != mapping.end()) {
        return mapping[i];
    }
    
    mapping[i] = DP(i / P, P, Q) + DP(i / Q, P, Q);
    
    return mapping[i];
}

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    long long N, P, Q;
    cin >> N >> P >> Q;

    mapping[0] = 1; 

    cout << DP(N, P, Q) << '\n';

    return 0;
}
// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int n;
//     cin >> n;
    
//     deque<int> deq; 
//     long now = 1;
    
//     while (now * now <= n) {
//         deq.push_back(now * now);
//         now++;
//     }
    
//     int rst = 0;
//     while (n > 0) {
//         int largest_square = deq.back();
        
//         if (n >= largest_square) {
//             rst += 1;
//             n -= largest_square;
//         } 
        
//         else {
//             deq.pop_back();
//         }
//     }
    
//     cout << rst << '\n';
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;

    for (int i = 1; i * i <= n; i++) {
        int square = i * i;
        for (int j = square; j <= n; j++) {
            dp[j] = min(dp[j], dp[j - square] + 1);
        }
    }

    cout << dp[n] << '\n';
    return 0;
}

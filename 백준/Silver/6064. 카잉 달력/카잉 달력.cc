// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int T;
//     cin >> T;
    
//     for (int i = 0; i < T; i++) {
//         int M, N, x, y;
//         cin >> M >> N >> x >> y;
        
//         int cx = 1, cy = 1;
//         int cnt = 1;
//         int token = 0;
        
//         while (cx != x || cy != y) {
//             if (cx > M && cy > N) {
//                 token = 1;
//                 break;
//             }
            
//             if (cx < M) {
//                 cx += 1;
//             }
            
//             else {
//                 cx = 1;
//             }
            
//             if (cy < N) {
//                 cy += 1;
//             }
            
//             else {
//                 cy = 1;
//             }
            
//             cnt += 1;
//         }
        
//         if (token == 0) {
//             cout << cnt << '\n';
//         }
        
//         else {
//             cout << -1 << '\n';
//         }
//     }
    
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int gcd (int a, int b) { // 유클리드 호제법
    while (b != 0) {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int lcm (int a, int b) {
    return a * b / gcd(a, b);
}

int main() {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int M, N, x, y;
        cin >> M >> N >> x >> y;
        int LCM = lcm(M, N);
        bool found = false; 
        
        for (int j = x; j <= LCM; j += M) {
            int val = (j % N == 0) ? N : j % N;
            
            if (val == y) {
                cout << j << '\n';
                found = true; 
                break;
            }
        }
        
        if (!found) { 
            cout << "-1" << '\n';
        }
    }
    
    return 0;
}

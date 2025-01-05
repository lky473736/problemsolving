// #include <bits/stdc++.h>
// using namespace std;
// typedef long long ll;

// int main(void) {
//     ios::sync_with_stdio(false); cin.tie(0);
    
//     int N; cin >> N;
//     if (N == 1) cout << "J7";
//     else if (N == 2) cout << "K8";
//     else if (N == 3) cout << "L9";
//     else {
//         int rest = N % 60 - 3;
//         char alpha[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'};
//         int num[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
        
//         int idx_alpha = 0, idx_num = 0;
//         for (int i = 0; i < rest; i++) {
//             int tk_alpha = 0, tk_num = 0;
//             if (idx_alpha == 12) {
//                 idx_alpha = 1;
//                 tk_alpha = 1;
//             }
//             if (idx_num == 10) {
//                 idx_num = 1;
//                 tk_num = 1;
//             }
//             if (tk_alpha != 1) {
//                 idx_alpha++;
//             } 
//             if (tk_num != 1) {
//                 idx_num++;
//             }
//         }
//         cout << alpha[idx_alpha-1] << num[idx_num-1];
//     }
        
//     return 0;
// }

#include <iostream>
int main() {
	int N;
	std::cin >> N;
	std::cout << (char)((N + 8) % 12+'A') << (N + 6) % 10 << std::endl;
	return 0;
}
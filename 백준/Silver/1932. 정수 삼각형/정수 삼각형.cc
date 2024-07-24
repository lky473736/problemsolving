// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int n;
//     cin >> n;
    
//     int arr[502][502] = {0};
//     int memory[502][502] = {0};
    
//     for (int i = 1; i <= n; i++) {
//         for (int j = 1; j <= i; j++) {
//             cin >> arr[i][j];
//         }
//     }
    
//     // for (int i = 1; i <= n; i++) {
//     //     for (int j = 0; j < i; j++) {
//     //         cout << arr[i-1][j];
//     //     }
//     // }
    
//     memory[1][1] = arr[1][1];
    
//     for (int i = 2; i <= n; i++) {
//         for (int j = 1; j <= i; j++) {
//             memory[i][j] = max(memory[i-1][j-1], memory[i][j]) + arr[i][j]; 
//             // 대각선 중 누가 더 큰지 비교하고 그걸 지금 있는거랑 더하기
//         }
//     }
    
//     int rst = memory[n][1];
//     for (int i = 1; i <= n; i++) {
//         if (rst < memory[n][i]) {
//             rst = memory[n][i];
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
    
    int arr[502][502] = {0};
    int memory[502][502] = {0};
    
    // Input the triangle values
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cin >> arr[i][j];
        }
    }
    
    // Initialize the top of the triangle
    memory[1][1] = arr[1][1];
    
    // Populate the memory array with the maximum sums
    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            // If j > 1, it means there's a valid upper-left diagonal to consider
            if (j > 1) {
                memory[i][j] = max(memory[i][j], memory[i-1][j-1] + arr[i][j]);
            }
            // If j <= i-1, it means there's a valid upper diagonal to consider
            if (j <= i-1) {
                memory[i][j] = max(memory[i][j], memory[i-1][j] + arr[i][j]);
            }
        }
    }
    
    // Find the maximum value in the last row of the memory array
    int rst = 0;
    for (int i = 1; i <= n; i++) {
        rst = max(rst, memory[n][i]);
    }
    
    cout << rst << '\n';
    
    return 0;
}
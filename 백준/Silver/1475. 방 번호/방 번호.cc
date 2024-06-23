// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     ios::sync_with_stdio(0);
//     cin.tie(0);
    
//     int arr[10] = {};
//     int cnt = 1;
    
//     string N;
//     cin >> N;
    
//     for (char &c : N) {
//         cout << c << '\n';
//         if (arr[int(c) - 48] != 0) {
//             if (c == '6') {
//                 if (arr[int(c) - 48 + 3] != 0) {
//                     cnt++;
//                     fill(arr, arr+10, 0);
//                     arr[int(c) - 48 + 3] = 1;
//                 }
                
//                 else {
//                     arr[int(c) - 48 + 3] = 1;
//                 }
//             }
            
//             else if (c == '9') {
//                 if (arr[int(c) - 48 - 3] != 0) {
//                     cnt++;
//                     fill(arr, arr+10, 0);
//                     arr[int(c) - 48 + 3] = 1;
//                 }
                
//                 else {
//                     arr[int(c) - 48 - 3] = 1;
//                 }
//             }
            
//             else {
//                 cnt++;
//                 fill(arr, arr+10, 0);
//                 arr[int(c) - 48 + 3] = 1;
//             }
//         }
        
//         else {
//             arr[int(c) - 48] = 1;
//         }
        
//         for (int i = 0; i < 10; i++) {
//             cout << arr[i] << ' ';
//         }
        
//         cout << ' ' << endl;
//     }
    
//     cout << cnt;
    
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int cnt = 1, token = 0;
    
    string N;
    cin >> N;
    
    int *space = new int[N.size()];
    
    while (true) {
        fill(arr, arr+10, 0);
        
        for (int i = 0; i < N.size(); i++) {
            int index = int(N[i]) - 48;
            
            if (space[i] == 1) { 
                continue;
            }
            
            else {
                if (arr[index] != 0) {
                    if (N[i] == '6') {
                        if (arr[9] != 0) {
                            continue;
                        } 
                        
                        else {
                            arr[9] = 1;
                            space[i] = 1;
                            token++;
                        }
                    } 
                    
                    else if (N[i] == '9') {
                        if (arr[6] != 0) {
                            continue;
                        } 
                        
                        else {
                            arr[6] = 1;
                            space[i] = 1;
                            token++;
                        }
                    } 
                    
                    else {
                        continue;
                    }
                }
                
                else {
                    space[i] = 1;
                    arr[index] = 1;
                    token++;
                }
            }
        }
        
        if (token == N.size()) {
            break;
        }
        
        cnt++;
    }
    
    cout << cnt;
    
    return 0;
}
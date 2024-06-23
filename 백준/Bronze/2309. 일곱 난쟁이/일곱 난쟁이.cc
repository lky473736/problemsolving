#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int arr[9];
    
    for (int i = 0; i < 9; i++) {
        cin >> arr[i];
    }
    
    for (int a = 0; a < 9; a++) {
        for (int b = 0; b < 9; b++) {
            if (a == b) {
                continue;
            }
            for (int c = 0; c < 9; c++) {
                if (a == c || b == c) {
                    continue;
                }
                for (int d = 0; d < 9; d++) {
                    if (a == d || b == d || c == d) {
                        continue;
                    }
                    for (int e = 0; e < 9; e++) {
                        if (a == e || b == e || c == e || d == e) {
                            continue;
                        }
                        for (int f = 0; f < 9; f++) {
                            if (a == f || b == f || c == f || d == f || e == f) {
                                continue;
                            }
                            for (int g = 0; g < 9; g++) {
                                if (a == g || b == g || c == g || d == g || e == g || f == g) {
                                    continue;
                                }
                                
                                if (arr[a] + arr[b] + arr[c] + arr[d] + arr[e] + arr[f] + arr[g] == 100) {
                                    int rst[7] = {arr[a], arr[b], arr[c], arr[d], arr[e], arr[f], arr[g]};
                                    sort (rst, rst+7);
                                    
                                    for (int x = 0; x < 7; x++) {
                                        cout << rst[x] << '\n';
                                    }
                                
                                    return 0;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
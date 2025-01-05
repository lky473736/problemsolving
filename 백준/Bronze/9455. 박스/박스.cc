#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(nullptr);
    
    int T; cin >> T;
    for (int i = 0; i < T; i++) {
        int r, c; 
        cin >> r >> c;
        
        int** arr = new int*[r];
        for(int i = 0; i < r; i++)
        	arr[i] = new int[c];

        for (int j = 0; j < r; j++) {
            for (int k = 0; k < c; k++) {
                cin >> arr[j][k];
            }
        }
        
        int cnt = 0;
        for (int j = r-2; j >= 0; j--) {
            for (int k = 0; k < c; k++) {
                if (arr[j][k] == 1 && arr[j+1][k] == 0) {
                    int p = j;
                    while (true) {
                        if (p == r-1) {
                            break;
                        }
                        if (arr[p+1][k] == 1) {
                            break;
                        }
                        else {
                            arr[p][k] = 0;
                            p++;
                            arr[p][k] = 1;
                            cnt++;
                        }
                    }
                }
            }
        }
        
        // cout << "---------" << i << '\n';
        // for (int j = 0; j < r; j++) {
        //     for (int k = 0; k < c; k++) {
        //         cout << arr[j][k] << ' ';       
        //     }
        //     cout << '\n';
        // }
        cout << cnt << '\n';
    }
    
    return 0;
}
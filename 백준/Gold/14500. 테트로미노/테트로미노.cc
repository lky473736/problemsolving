#include <bits/stdc++.h>
#include <cstdio>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    
    // int** mat = new int*[N];
    // for (int i = 0; i < N; i++) {
    //     mat[i] = new int[M];
    // }
    
    vector<vector<int>> mat(N, vector<int>(M));
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> mat[i][j];
        }
    }
    
    vector<int> tetro;
    int sumation = 0;
    int max_num = 0;
    
    // 0000
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M-3; j++) {
            // cout << i << j << '\n';
            sumation = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i][j+3];
            // cout << sumation << '\n';
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 0
    // 0
    // 0
    // 0
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N-3; j++) {
            sumation = mat[j][i] + mat[j+1][i] + mat[j+2][i] + mat[j+3][i];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 00
    // 00
    for (int i = 0; i < N-1; i++) {
        for (int j = 0; j < M-1; j++) {
            sumation = mat[i][j] + mat[i][j+1] + mat[i+1][j] + mat[i+1][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 0      0
    // 0      0
    // 00 or 00
    for (int i = 0; i < N-2; i++) {
        for (int j = 0; j < M-1; j++) {
            sumation = mat[i][j] + mat[i+1][j] + mat[i+2][j] + mat[i+2][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
            
            sumation = mat[i][j+1] + mat[i+1][j+1] + mat[i+2][j] + mat[i+2][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 00  00
    // 0    0
    // 0 or 0
    for (int i = 0; i < N-2; i++) {
        for (int j = 0; j < M-1; j++) {
            sumation = mat[i][j] + mat[i+1][j] + mat[i+2][j] + mat[i][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
            
            sumation = mat[i][j] + mat[i][j+1] + mat[i+1][j+1] + mat[i+2][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 0        0
    // 000 or 000
    for (int i = 0; i < N-1; i++) {
        for (int j = 0; j < M-2; j++) {
            sumation = mat[i][j] + mat[i+1][j] + mat[i+1][j+1] + mat[i+1][j+2];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
            
            sumation = mat[i+1][j] + mat[i+1][j+1] + mat[i+1][j+2] + mat[i][j+2];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 000 or 000
    // 0        0
    for (int i = 0; i < N-1; i++) {
        for (int j = 0; j < M-2; j++) {
            sumation = mat[i][j] + mat[i+1][j] + mat[i][j+1] + mat[i][j+2];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
            
            sumation = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+2];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 0      0 
    // 00    00 
    //  0 or 0
    for (int i = 0; i < N-2; i++) {
        for (int j = 0; j < M-1; j++) {
            sumation = mat[i][j] + mat[i+1][j] + mat[i+1][j+1] + mat[i+2][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
            
            sumation = mat[i][j+1] + mat[i+1][j+1] + mat[i+1][j] + mat[i+2][j];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    //  00  00
    // 00 or 00
    for (int i = 0; i < N-1; i++) {
        for (int j = 0; j < M-2; j++) {
            sumation = mat[i][j+1] + mat[i][j+2] + mat[i+1][j] + mat[i+1][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
            
            sumation = mat[i][j] + mat[i][j+1] + mat[i+1][j+1] + mat[i+1][j+2];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 000    0
    //  0 or 000
    for (int i = 0; i < N-1; i++) {
        for (int j = 0; j < M-2; j++) {
            sumation = mat[i][j] + mat[i][j+1] + mat[i][j+2] + mat[i+1][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
            
            sumation = mat[i+1][j] + mat[i+1][j+1] + mat[i+1][j+2] + mat[i][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    // 0      0
    // 00 or 00
    // 0      0
    for (int i = 0; i < N-2; i++) {
        for (int j = 0; j < M-1; j++) {
            sumation = mat[i][j] + mat[i+1][j] + mat[i+2][j] + mat[i+1][j+1];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
            
            sumation = mat[i][j+1] + mat[i+1][j+1] + mat[i+2][j+1] + mat[i+1][j];
            tetro.push_back (sumation);
            
            if (sumation > max_num) {
                max_num = sumation;
            }
        }
    }
    
    cout << max_num << '\n';
    
    return 0;
}
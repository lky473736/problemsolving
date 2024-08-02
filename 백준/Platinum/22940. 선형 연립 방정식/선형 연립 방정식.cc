#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N;
    cin >> N;

    double solve[100];
    double matrix[100][101];  
    int length = 0;
    
    int cnt = 0;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j <= N; ++j) {
            cin >> matrix[i][j];
        }
    }

    for (int i = 0; i < N; ++i) {
        double divider = matrix[i][i];
        
        for (int j = 0; j <= N; ++j) {
            matrix[i][j] /= divider; // diagonal == 1
        }

        for (int j = 0; j < N; ++j) {
            if (i != j) {
                double factor = matrix[j][i];
                
                for (int k = 0; k <= N; ++k) {
                    matrix[j][k] -= factor * matrix[i][k];
                }
            }
            
            else {
                ;
            }
        }
    }

    for (int i = 0; i < N; ++i) {
        solve[cnt] = matrix[i][N];
        cout << solve[cnt++] << ' ';
        // https://velog.io/@nada_dbstkddl/C-%EC%86%8C%EC%88%98%EC%9E%90%EB%A6%AC%EC%88%98-%EB%8B%A4%EB%A3%A8%EA%B8%B0-precision-fixed
    }

    return 0;
}

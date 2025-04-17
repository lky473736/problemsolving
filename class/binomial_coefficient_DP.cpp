#include <bits/stdc++.h>
using namespace std;

int **B = new int*[5];  

int bin(int n, int k) {
    // dynamic programming to calculate binomial coefficients
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= min(i, k); j++) {
            if (j == 0 || j == i) {
                B[i][j] = 1;  // base case
            } else {
                B[i][j] = B[i-1][j-1] + B[i-1][j];  // recurrence relation
            }
        }
    }
    return B[n][k];
}

int main() {
    for (int i = 0; i < 5; i++) {
        B[i] = new int[4];
    }
    cout << bin(4, 3) << endl;  // C(4,3) = 4

    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 4; j++) {
            cout << B[i][j] << ' ';
        }
        cout << endl;
    }

    return 0;
}

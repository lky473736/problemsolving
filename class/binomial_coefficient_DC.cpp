#include <bits/stdc++.h>
using namespace std;

int bin (int n, int k) {
    // recursive way (divide and conquer)
    if (k == 0 || k == n) {
        return 1;
    } else {
        return bin (n-1, k-1) + bin (n-1, k);
    }
}

int main() {
    for (int i = 0; i < 5; i++) {
        cout << bin(4, i) << '\n';
    }
}

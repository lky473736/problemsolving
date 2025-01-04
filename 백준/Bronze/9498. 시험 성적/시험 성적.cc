#include <bits/stdc++.h>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);

    int A;
    cin >> A;
    char c;

    if (A >= 90) {
        c = 'A';
    } 
    else if (A >= 80) {
        c = 'B';
    }
    else if (A >= 70) { 
        c = 'C';
    }
    else if (A >= 60) {
        c = 'D';
    }
    else {
        c = 'F';
    }

    cout << c;

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> slist(2 * n); 

    for (int i = 0; i < 2 * n; i++) {
        cin >> slist[i];
    }

    sort(slist.begin(), slist.end()); 

    int semi = INT_MAX;
    for (int i = 0; i < n; i++) {
        semi = min(semi, slist[i] + slist[2 * n - 1 - i]);
    }

    cout << semi << '\n'; 

    return 0;
}
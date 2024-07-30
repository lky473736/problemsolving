#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> sequence;
    
    for (int i = 1; i < 100; ++i) {
        for (int j = 0; j < i; ++j) {
            sequence.push_back(i);
        }
    }
    
    int a, b;
    cin >> a >> b;

    --a; --b;

    int sum = 0;
    for (int i = a; i <= b; ++i) {
        sum += sequence[i];
    }
    
    cout << sum;

    return 0;
}

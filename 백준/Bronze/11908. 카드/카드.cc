#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int N; cin >> N;
    int sum = 0;
    int compo = 0;
    
    if (N != 1) {
        int max = 0;
        for (int i = 0; i < N; i++) {
            cin >> compo;
            sum += compo;
            if (max < compo) {
                max = compo;
            }
        }
        cout << sum-max;
    } else {
        cin >> compo;
        cout << 0;
    }
    
    return 0;
}

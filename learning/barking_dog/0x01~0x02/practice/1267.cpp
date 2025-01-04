#include <bits/stdc++.h>
using namespace std;
// typedef long long ll;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int N; cin >> N; 
    vector<int> arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];

    int y_sum = 0;
    int m_sum = 0;

    for (int i = 0; i < N; i++) {
        y_sum += ((arr[i] / 30) + 1) * 10;
        m_sum += ((arr[i] / 60) + 1) * 15; 
    }

    if (y_sum == m_sum) cout << "Y M " << y_sum;
    else {
        if (y_sum > m_sum) cout << "M " << m_sum;
        else cout << "Y " << y_sum;
    }

    return 0;
}
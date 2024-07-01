#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    long long N;
    cin >> N;
    
    if (N == 1) {
        cout << 1;
        return 0;
    }
    
    queue<long long> q;
    for (long long i = 1; i <= N; i++) {
        q.push(i);
    }
    
    while (true) {
        q.pop();
        
        if (q.size() == 1) {
            break;
        }
        
        long long temp = q.front();
        q.pop();
        q.push(temp);
    }
    
    cout << q.front();
    
    return 0;
}
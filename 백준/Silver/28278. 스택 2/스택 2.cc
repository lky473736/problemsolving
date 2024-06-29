#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    stack<long long> s;
    long long cnt = 0; 
    
    long long N;
    cin >> N;
    
    for (long long i = 0; i < N; i++) {
        int command;
        cin >> command;
        
        if (command == 1) { 
            int X;
            cin >> X;
            
            s.push(X);
            cnt++;
        }
        
        else if (command == 2) {
            if (cnt != 0) {
                cout << s.top() << '\n';
                s.pop();
                cnt--;
            } 
            
            else {
                cout << -1 << '\n';;
            }
        }
        
        else if (command == 3) {
            cout << cnt << '\n';
        }
        
        else if (command == 4) {
            cout << s.empty() << '\n';
        }
        
        else if (command == 5) {
            if (!s.empty()) { 
                cout << s.top() << '\n';
            } 
            
            else {
                cout << -1 << '\n';
            }
        }
    }
    
    return 0;
}

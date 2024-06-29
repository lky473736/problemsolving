#include <bits/stdc++.h>
using namespace std;

int main() {
    stack<int> s;
    int cnt = 0; 
    
    int N;
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        string command;
        cin >> command;
        
        if (command == "push") { 
            int X;
            cin >> X;
            
            s.push(X);
            cnt++;
        }
        
        else if (command == "pop") {
            if (cnt != 0) {
                cout << s.top() << '\n';
                s.pop();
                cnt--;
            } 
            
            else {
                cout << -1 << '\n';;
            }
        }
        
        else if (command == "size") {
            cout << cnt << '\n';
        }
        
        else if (command == "empty") {
            cout << s.empty() << '\n';
        }
        
        else if (command == "top") {
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

#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int rst = 0;
    
    cin >> s;
    stack<char> brace;
    
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '(') {
            brace.push(s[i]);
        }
        
        else {
            if (s[i-1] == '(') {
                brace.pop();
                rst += brace.size();
            }
            
            else {
                brace.pop();
                rst++;
            }
        }
    }
    
    cout << rst;
    
    return 0;
}
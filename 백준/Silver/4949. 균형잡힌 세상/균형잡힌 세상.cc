#include <bits/stdc++.h>
using namespace std;

int main() {
    while (true) {
        int cnt = 0, token = 0;
        stack<char> brace;
        
        string sentence;
        getline(cin, sentence);
        
        for (char input : sentence) {
            if (input == '.') {
                if (cnt == 0) {
                    token = 1;
                    break;
                }
                
                else {
                    if (brace.empty()) {
                        cout << "yes" << '\n';
                    }
                    
                    else {
                        cout << "no" << '\n';
                    }
                    
                    break;
                }
            }
            
            else {
                if (input == '(' || input == '[') {
                    brace.push(input);
                }
                
                else if (input == ')') {
                    if (!brace.empty() && brace.top() == '(') {
                        brace.pop();
                    }
                    
                    else {
                        brace.push(input);
                    }
                }
                
                else if (input == ']') {
                    if (!brace.empty() && brace.top() == '[') {
                        brace.pop();
                    }
                    
                    else {
                        brace.push(input);
                    }
                }
            }
            
            cnt++;
        }
        
        if (token == 1) {
            break;
        }
    }
    
    return 0;
}
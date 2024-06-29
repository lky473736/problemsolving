#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    stack<int> s;
    int obj[100001];
    
    int n; 
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        int compo;
        cin >> compo;
        obj[i] = compo;
    }
    
    int chan = 0;
    int num = 1;
    int token = 0;
    int *oper = new int[2 * n]; // 1 : -. 2 : +
    int cnt = 0;
    
    while (chan < n) {
        if (!s.empty() && obj[chan] <= s.top()) {
            if (obj[chan] == s.top()) {
                oper[cnt++] = 1;
                s.pop();
                chan++;
            } 
            
            else {
                token = 1;
                break;
            }
        } 
        
        else {
            oper[cnt++] = 2;
            s.push(num++);
        }
    }
    
    if (token == 1) { 
        cout << "NO\n";
    } 
    
    else {
        for (int i = 0; i < cnt; i++) {
            if (oper[i] == 1) {
                cout << "-\n";
            } 
            
            else {
                cout << "+\n";
            }
        }
    }
    
    return 0;
}
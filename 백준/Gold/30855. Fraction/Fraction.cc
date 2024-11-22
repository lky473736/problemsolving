#include <bits/stdc++.h>
using namespace std;

long long gcd (string c1, string c2) {
    long long a = stoll(c1);
    long long b = stoll(c2);
    
    if (b == 0) {
        return a;
    }
    
    else {
        return gcd(to_string(b), to_string(a%b));
    }
}

pair<string, string> solve (long long a1, long long a2, long long b1, long long b2, long long c1, long long c2) {
    long long p1 = a2*b1*c2+a1*b2*c1;
    long long p2 = a1*b1*c2;
    return {to_string(p1), to_string(p2)};
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    long long n;
    cin >> n;
    
    stack<pair<string, string>> st;
    pair<string, string> compo;
    
    int open = 0;
    int close = 0;
    
    for (long long i = 0; i < n; i++) {
        string temp;
        cin >> temp;
        
        compo = {temp, "1"};
        
        if (compo.first == ")") {
            if (i == 0) {
                goto k;
            }
            if (st.top().first == "(") {
                goto k;
            }
            close++;
            
            long long c2 = stoll(st.top().first);
            long long c1 = stoll(st.top().second);
            if (st.empty()) {
                goto k;
            }
            st.pop();
            if (st.top().first == "(") {
                goto k;
            }
            
            long long b2 = stoll(st.top().first);
            long long b1 = stoll(st.top().second);
            if (st.empty()) {
                goto k;
            }
            st.pop();
            if (st.top().first == "(") {
                goto k;
            }
            
            long long a2 = stoll(st.top().first);
            long long a1 = stoll(st.top().second);
            if (st.empty()) {
                goto k;
            }
            st.pop();
            st.pop();
            
            pair<string, string> rst = solve(a1, a2, b1, b2, c1, c2);
            st.push (rst);
        }
        
        else {
            if (i == 0 && compo.first != "(") {
                goto k;
            }
            if (compo.first == "(") {
                open++;
            }
            st.push(compo);
        }
    }
    
    if (open == close && open != 0 && close != 0) {
        pair<string, string> topping = st.top();
        st.pop();
        
        if (!st.empty()) {
            goto k;
        }
        cout << stoll(topping.first) / gcd(topping.first, topping.second) << ' ' << stoll(topping.second) / gcd(topping.first, topping.second);
        return 0;
    }
    
k :
    cout << "-1";    
    return 0;
}
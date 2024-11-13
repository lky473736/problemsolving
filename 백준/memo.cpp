#include <bits/stdc++.h>
using namespace std;

int divide(int A, int B) {
    if (B == 0) return abs(A);
    return divide(B, A % B);
}

pair<string, string> get(pair<string, string> a, pair<string, string> b, pair<string, string> c) {
    string s1 = to_string(stoi(a.second) * stoi(b.first) * stoi(c.second) + stoi(a.first) * (stoi(b.second) * stoi(c.first)));
    string s2 = to_string(stoi(a.second) * (stoi(b.second) * stoi(c.first)));
    return {s1, s2};
}

int main() {
    int n;
    cin >> n;

    stack<pair<string, string>> st;
    int cnt_left = 0, cnt_right = 0;

    for (int i = 0; i < n; i++) {
        string compo;
        cin >> compo;

        if (compo == "(") {
            cnt_left++;
            st.push({compo, "0"});
        } 
        else if (compo == ")") {
            cnt_right++;

            if (st.size() < 4) { 
                cout << "-1";
                return 0;
            }

            pair<string, string> c = st.top(); st.pop();
            pair<string, string> b = st.top(); st.pop();
            pair<string, string> a = st.top(); st.pop();

            if (st.empty() || st.top().first != "(") { 
                cout << "-1";
                return 0;
            }
            st.pop();

            pair<string, string> formula = get(a, b, c);
            st.push(formula);
        } 
        else { 
            st.push({compo, "1"});
        }
    }

    if (cnt_left != cnt_right || st.size() != 1 || st.top().second == "0") { 
        cout << "-1";
        return 0;
    }

    pair<string, string> fraction = st.top();
    int GCD = divide(stoi(fraction.first), stoi(fraction.second));
    cout << stoi(fraction.first) / GCD << ' ' << stoi(fraction.second) / GCD;
}

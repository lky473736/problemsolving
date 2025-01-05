#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(void) {
    ios::sync_with_stdio(0); cin.tie(nullptr);
    
    string str; cin >> str;
    for (int i = 0; i < str.size(); i++) {
        if (str[i] == 'B') cout << 'v';
        else if (str[i] == 'E') cout << "ye";
        else if (str[i] == 'H') cout << "n";
        else if (str[i] == 'P') cout << "r";
        else if (str[i] == 'C') cout << "s";
        else if (str[i] == 'Y') cout << "u";
        else if (str[i] == 'X') cout << "h";
        else cout << char(str[i]+32);
    }
    
    return 0;
}
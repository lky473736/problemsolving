#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);

    int N, M; cin >> N >> M;

    set<string> unheard;  
    vector<string> result; 

    string name;
    for (int i = 0; i < N; ++i) {
        cin >> name;
        unheard.insert(name);
    }

    for (int i = 0; i < M; ++i) {
        cin >> name;
        if (unheard.find(name) != unheard.end()) {
            result.push_back(name);
        }
    }

    sort(result.begin(), result.end()); 

    cout << result.size() << '\n';
    for (const auto &n : result)
        cout << n << '\n';

    return 0;
}

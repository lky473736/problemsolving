#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    unordered_map<int, int> problems;
    map<int, set<int>> levels; 

    for (int i = 0; i < N; ++i) {
        int P, L;
        cin >> P >> L;
        
        problems[P] = L;
        levels[L].insert(P);
    }

    int M;
    cin >> M;

    for (int i = 0; i < M; ++i) {
        string command;
        cin >> command;

        if (command == "recommend") {
            int x;
            cin >> x;
            if (x == 1) {
                auto it = prev(levels.end());
                cout << *(it->second.rbegin()) << "\n";
            } 
            
            if (x == -1) {
                auto it = levels.begin();
                cout << *(it->second.begin()) << "\n";
            }
        } 
        
        else if (command == "add") {
            int P, L;
            cin >> P >> L;
            
            problems[P] = L;
            levels[L].insert(P);
        } 
        
        else if (command == "solved") {
            int P;
            cin >> P;
        
            int L = problems[P];
            
            levels[L].erase(P);
            
            if (levels[L].empty()) {
                levels.erase(L);
            }
            
            problems.erase(P);
        }
    }

    return 0;
}
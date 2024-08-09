#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, m;
    cin >> n;
    
    unordered_map<int, pair<int, int>> problem; // 번호, (난이도, 알고리즘)
    unordered_map<int, set<pair<int, int>>> groups; // 분류, (난이도, 번호)
    map<int, set<int>> level_groups; // 난이도, 번호

    // 입력
    for (int i = 0; i < n; ++i) {
        int id, level, group;
        cin >> id >> level >> group;
        
        problem[id] = {level, group};
        groups[group].insert({level, id});
        level_groups[level].insert(id);
    }

    cin >> m;

    for (int i = 0; i < m; ++i) {
        string command;
        cin >> command;

        if (command == "recommend") {
            int group, x;
            cin >> group >> x;
            
            if (x == 1) { // 특정 그룹 가장 어려움
                auto pointer = prev(groups[group].end());
                cout << pointer->second << "\n";
            } 
            
            else { // 특정 그룹 가장 쉬움
                auto pointer = groups[group].begin();
                cout << pointer->second << "\n";
            }
        } 
        
        else if (command == "recommend2") {
            int x;
            cin >> x;
            if (x == 1) { // 전체 가장 어려움
                auto pointer = prev(level_groups.rbegin()->second.end());
                cout << *pointer << "\n";
            } 
            
            else { // 전체 가장 쉬움
                auto pointer = level_groups.begin()->second.begin();
                cout << *pointer << "\n";
            }
        } 
        
        else if (command == "recommend3") {
            int x, level;
            cin >> x >> level;
            
            if (x == 1) { // 난이도 이하에서 가장 쉬움
                auto pointer = level_groups.lower_bound(level);
                
                if (pointer == level_groups.end()) {
                    cout << "-1\n";
                } 
                
                else {
                    cout << *(pointer->second.begin()) << "\n";
                }
            } 
            
            else { // 난이도 이하에서 가장 어려움
                auto pointer = level_groups.lower_bound(level);
                
                if (pointer == level_groups.begin()) {
                    cout << "-1\n";
                } 
                
                else {
                    pointer = prev(pointer);
                    cout << *(pointer->second.rbegin()) << "\n";
                }
            }
        } 
        
        else if (command == "add") {
            int id, level, group;
            cin >> id >> level >> group;
            
            problem[id] = {level, group}; 
            groups[group].insert({level, id}); // add
            level_groups[level].insert(id);
        } 
        
        else if (command == "solved") {
            int id;
            cin >> id;
            
            int level = problem[id].first;
            int group = problem[id].second;

            groups[group].erase({level, id}); // solved니깐 제거
            if (groups[group].empty()) {
                groups.erase(group);
            }

            level_groups[level].erase(id);
            if (level_groups[level].empty()) {
                level_groups.erase(level);
            }

            problem.erase(id);
        }
    }

    return 0;
}

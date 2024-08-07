#include <bits/stdc++.h>
using namespace std;

int main() {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
    
    int t;
    cin >> t;
    
    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        
        unordered_map<string, vector<string>> clothes;
        
        for (int j = 0; j < n; j++) {
            string name, sort;
            cin >> name >> sort;
            
            clothes[sort].push_back(name);
        }
        
        vector<int> list_length;
        for (auto& kv : clothes) {
            list_length.push_back(kv.second.size());
        }
        
        int counting = 1;
        for (int len : list_length) {
            counting *= (len + 1);
        }
        
        counting -= 1;
        
        cout << counting << endl;
    }
    
    return 0;
}

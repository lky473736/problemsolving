// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     // unordered_map<string, vector<int>> amap;
//     unordered_set<string> aset;
//     vector<string> aqueue;
    
//     long long K, L;
//     cin >> K >> L; 
    
//     int sequence = 0; 
    
//     for (int i = 0; i < L; i++) {
//         string number;
//         cin >> number;
        
//         if (aset.find(number) == aset.end()) {
//             aset.erase(number);
//         }
        
//         aset.insert(number);
//     }
    
//     int i = 0;
//     for (auto point = aset.begin(); point != aset.end(); point++) {
//         aqueue.push_back(*point);
//     }
    
//     // for (const auto& num : aqueue) {
//     //     cout << aqueue[i] << ' ';
//     // }
    
//     for (int i = aqueue.size()-1; i > 0; i--) {
//         cout << aqueue[i] << '\n';
//     }
    
//     // int rest_cnt = K;
//     // int cnt = 0;
    
//     // while (rest_cnt != 0) {
//     //     if (amap[aqueue.front()][1] < cnt) {
//     //         rest_cnt--;
//     //         cout << aqueue.front() << '\n';
//     //         aqueue.pop();
//     //     }
//     //     cnt++;
//     // }
    
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int main() {
    unordered_set<string> aset;
    vector<string> aqueue;
    unordered_map<string, int> last_posi;
    
    long long K, L;
    cin >> K >> L;
    
    for (int i = 0; i < L; i++) {
        string number;
        cin >> number;

        if (aset.find(number) != aset.end()) {
            aset.erase(number);
        }
        
        aset.insert(number);
        last_posi[number] = i; // 마지막으로 등장한 인덱스 넣기
    }
    
    vector<pair<int, string>> for_sort; // 정렬해야 하니깐
    for (const auto& num : aset) { 
        for_sort.push_back(make_pair(last_posi[num], num));
    }

    sort(for_sort.begin(), for_sort.end()); // 정렬 (last_posi 기준으로 해서)

    long long vector_size = for_sort.size();
    for (long long i = 0; i < min(K, vector_size); i++) {
        cout << for_sort[i].second << '\n';
    }
    
    return 0;
}
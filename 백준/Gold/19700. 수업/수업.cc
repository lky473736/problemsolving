/*
    키가 큰 순으로 내림차순
    -> 팀 넣기 
        -> 최대한 팀 적게해야하니깐 가능하면 인원이 많은 팀에 배치
        -> 만약 없으면 팀 만들기 
*/

/* 첫번째 시도 */

// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     long long N;
//     cin >> N;
    
//     vector<vector<int>> arr;
    
//     for (int i = 0; i < N; i++) {
//         long long hi, ki; 
//         cin >> hi >> ki;
        
//         arr.push_back({hi, ki});
//     }
    
//     sort(arr.rbegin(), arr.rend()); // 내림차순
    
//     map<long long, int> dict_num; 
//     vector<long long> keys;       
    
//     for (int i = 0; i < N; i++) {
//         long long cur_hei = arr[i][0];
//         long long cur_team = -1; // 일종의 token 역할
//         int max_size = -1; 
    
//         for (long long key : keys) { // 인원 가장 많은 팀
//             if (key >= cur_hei && dict_num[key] >= max_size) {
//                 max_size = dict_num[key];
//                 cur_team = key;
//             }
//         }
        
//         if (cur_team != -1) {  // team 있으면 넣기
//             dict_num[cur_team]++;
//         }
         
//         else {  // 없으면 만들기
//             keys.push_back(cur_hei);
//             dict_num[cur_hei] = 1;
//         }
//     }
    
//     cout << keys.size();
    
//     return 0;
// }

/* 두번째 시도 */

// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int N;
//     cin >> N;
    
//     vector<pair<int, int>> arr;
    
//     for (int i = 0; i < N; i++) {
//         int hi, ki; 
//         cin >> hi >> ki;
        
//         arr.push_back({hi, ki});
//     }
    
//     sort(arr.rbegin(), arr.rend()); // 내림차순
    
//     map<int, int> dict_num;  
//     vector<int> keys; 
    
//     for (int i = 0; i < N; i++) {
//         int cur_hei = arr[i].first; // 키
//         int cur_k = arr[i].second; // 인원수
        
//         int cur_team = -1;
//         int max_size = -1; 
    
//         for (int key : keys) { 
//             if (dict_num[key] >= cur_k && dict_num[key] > max_size) { 
//                 if (cur_hei > key) {
//                     max_size = dict_num[key];
//                     cur_team = key;
//                 }
//             }
//         }
        
//         if (cur_team != -1) { 
//             dict_num[cur_team] += 1;
//         } 
        
//         else {  
//             keys.push_back(cur_hei);
//             dict_num[cur_hei] = 1;
//         }
//     }
    
//     cout << keys.size() << endl;  
    
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    
    vector<pair<int, int>> arr(N); // 키, 최소사이즈
    
    for (int i = 0; i < N; i++) {
        int hi, ki; 
        cin >> hi >> ki;
        
        arr[i] = {hi, ki};
    }

    sort(arr.rbegin(), arr.rend());  // 내림차순 (키큰학생부터 / 그리디)
    
    multiset<int> teams; // multiset : 팀 인원수 저장 + 자동으로 정렬됨
    
    for (const auto& compo : arr) { // 순회
        int height = compo.first; // 현재 키
        int min_size = compo.second; 
        
        auto it = teams.lower_bound(min_size); 
        // 현재 학생 배정받을 가장 적은 팀 (min_size보다 큰 값중 최소값)
        
        if (it != teams.begin()) { // 그런 팀이 있다면
            --it; // -1해줘야 원하는 팀 나옴
            int cursor = *it; // 팀 현재 인원수
            
            teams.erase(it); // 삭제하고 아래서 업데이트
            teams.insert(cursor + 1); // 이렇게 업데이트 (추가해야 하니깐)
        } 
        
        else { // 그런 팀이 없다면
            teams.insert(1); // 팀생성
        }
    }

    cout << teams.size() << endl; 
    
    return 0;
}

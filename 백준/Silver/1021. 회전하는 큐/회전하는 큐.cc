#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N, M;
    cin >> N >> M;
    
    deque<int> dq;
    for (int i = 0; i < N; i++) {
        dq.push_back(i + 1);
    }
    
    vector<int> nums(M);
    for (int i = 0; i < M; i++) {
        cin >> nums[i];
    }
    
    int cnt = 0;
    for (int i = 0; i < M; i++) {
        int ind = 0;
        
        // 원하는 숫자의 인덱스를 찾음
        for (int j = 0; j < dq.size(); j++) {
            if (dq[j] == nums[i]) {
                ind = j;
                break;
            }
        }
        
        int half = dq.size() / 2;
        
        // 인덱스가 절반 이하인지 확인
        if (ind <= half) {
            // 왼쪽으로 회전
            for (int j = 0; j < ind; j++) {
                dq.push_back(dq.front());
                dq.pop_front();
                cnt++;
            }
        } else {
            // 오른쪽으로 회전
            for (int j = 0; j < dq.size() - ind; j++) {
                dq.push_front(dq.back());
                dq.pop_back();
                cnt++;
            }
        }
        
        // 숫자를 제거
        dq.pop_front();
    }
    
    cout << cnt;
    
    return 0;
}

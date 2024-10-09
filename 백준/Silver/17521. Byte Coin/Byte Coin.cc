#include <bits/stdc++.h>
using namespace std;

/*
    그냥 예시처럼 주가가 올라간다면 오늘 다 사고
    떨어질거 같으면 다 팔면 됨.
    이게 그리디가 맞는 지 모르겠는 문제
*/

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    long long n, w;
    cin >> n >> w; 
    
    vector<long long> p(n);

    for (long long i = 0; i < n; i++) {
        cin >> p[i]; // 이미 모든 걸 알고 있음 == 내일 내려갈지 올라갈지 알고 있음
    }

    long long rst = w, c = 0, cnt = 0; // 현재 돈 얼마? 코인 몇개? 

    for (long long i = 0; i < n - 1; i++) {
        if (p[i] < p[i + 1]) { // 내일 오를 거 같으면?
            cnt = rst / p[i]; // 지금 돈에서 살 수 있는 모든 코인 갯수
            rst -= cnt * p[i]; 
            c += cnt;
        }
        
        else { // 내일 내려갈 거 같으면?
            rst += c * p[i]; // 다 팔기
            c = 0;
        }
    }

    rst += c * p[n - 1]; // 마지막에 다 판다고 했으니깐 다 팔아버리기 (마지막일에는 다 파는거임 그니깐 n-1)
    cout << rst << '\n';
    
    return 0;
}

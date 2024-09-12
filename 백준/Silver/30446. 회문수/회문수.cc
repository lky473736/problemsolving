#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

string n;  // 입력으로 주어지는 문자열 n
char s[7]; // 팰린드롬을 생성하기 위한 배열
ll res;    // 팰린드롬의 개수를 저장할 변수

// 문자열 a가 b보다 작거나 같은지 비교하는 함수
bool comp(string a, string b) {
    if (a.size() != b.size()) return a.size() < b.size(); // 길이 비교
    return a <= b; // 사전 순 비교
}

// 깊이 우선 탐색을 이용해 팰린드롬을 생성하는 함수
void dfs(int d, int m) {
    // 현재 깊이가 주어진 길이 m과 같으면 팰린드롬 생성
    if (d == m) {
        if (s[0] == '0') return; // 앞자리가 0인 수는 무시
        string e = "", o = "";
        int i;
        
        // 팰린드롬의 짝수 자리수 생성
        for (i = 0; i < m; i++) {
            e += s[i];
            o += s[i];
        }
        for (i = 0; i < m; i++) e += s[m - i - 1];
        
        // 팰린드롬의 홀수 자리수 생성
        for (i = 1; i < m; i++) o += s[m - i - 1];
        
        // 생성한 팰린드롬이 n보다 작거나 같은지 확인하고 개수 추가
        res += (comp(e, n) + comp(o, n));
        return;
    }
    
    // 모든 숫자에 대해 재귀 호출
    char c;
    for (c = '0'; c <= '9'; c++) {
        s[d] = c; // 현재 자리수에 숫자를 대입
        dfs(d + 1, m); // 다음 자리수로 재귀 호출
    }
}

int main() {
    ios::sync_with_stdio(false); // C++의 입출력 속도를 향상시킴
    cin.tie(NULL); cout.tie(NULL); // 입출력 동기화 비활성화
    cin >> n; // 입력 읽기
    
    int i;
    // 1자리부터 5자리까지 팰린드롬을 생성
    for (i = 1; i <= 5; i++) dfs(0, i);
    
    cout << res; // 결과 출력
    return 0;
}

#include <bits/stdc++.h>
using namespace std;

const long long INF = 1000000000000000000; 

int main() {
    int n, m;
    cin >> n;
    cin >> m;

    vector<vector<long long>> mapping(n + 1, vector<long long>(n + 1, INF));

    for (int i = 1; i <= n; i++) {
        mapping[i][i] = 0; // diagonal == 0 (자기 자신으로 가는 경로)
    }

    for (int i = 0; i < m; i++) {
        int A, B;
        long long weight;
        cin >> A >> B >> weight;
        
        mapping[A][B] = min(mapping[A][B], weight); // 최솟값
    }

    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                // i->j로 가는거랑 i->k->j로 가는거랑 거리 비교해서 넣어놓기
                mapping[i][j] = min(mapping[i][j], mapping[i][k] + mapping[k][j]);
            }
        }
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (mapping[i][j] == INF) {
                cout << "0 ";
            } 
            
            else {
                cout << mapping[i][j] << " ";
            }
        }
        cout << '\n';
    }

    return 0;
}

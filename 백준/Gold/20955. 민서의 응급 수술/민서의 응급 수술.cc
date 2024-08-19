#include <bits/stdc++.h>
using namespace std;

vector<int> adjacent[100001];
bool visited[100001];
bool is_cycle[100001];

int cnt = 0;

void dfs (int current, int previous) {
    visited[current] = true;
    
    for (auto next : adjacent[current]) {
        if (visited[next] == false) {
            dfs(next, current);
        }
        
        else if (is_cycle[next] == false) { // 방문한 노드 다시만남
            if (next != previous) { // 근데 그게 부모가 아님
                cnt++; // cnt 1씩 증가
            }
        }
    }
    
    is_cycle[current] = true;
}

int main(){
    int n, m;
    cin >> n >> m;
    
    int rst = 0;
    
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        
        adjacent[u].push_back(v);
        adjacent[v].push_back(u);
    }
    
    for (int i = 1; i <= n; i++) {
        if (visited[i] == false) {
            dfs (i, 0);
            rst++;
        }
    }
    
    cout << cnt - 1 + rst;
}
#include <bits/stdc++.h>
using namespace std;

vector<int> adj;
vector<bool> visited;
vector<bool> finished;
int not_in_cycle;

void dfs(int node) {
    visited[node] = true;
    int next = adj[node];
    
    if (!visited[next]) {
        dfs(next);
    } else if (!finished[next]) {
        for (int i = next; i != node; i = adj[i]) {
            not_in_cycle--;
        }
        not_in_cycle--;
    }
    
    finished[node] = true;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int T;
    cin >> T;
    
    while (T--) {
        int n;
        cin >> n;
        
        adj.assign(n, 0);
        visited.assign(n, false);
        finished.assign(n, false);
        not_in_cycle = n;
        
        for (int i = 0; i < n; i++) {
            int compo;
            cin >> compo;
            adj[i] = compo - 1;
        }
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(i);
            }
        }
        
        cout << not_in_cycle << '\n';
    }
    
    return 0;
}

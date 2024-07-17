/*
    bfs한다 -> 4개 있다 -> 터뜨리기
                        -> 터뜨린 곳에는 . 남기 -> 중력 적용해야 함
            -> 4개 아니다 -> 터뜨리지 말고 일단 대기
*/

#include <bits/stdc++.h>
using namespace std;

char mapping[12][6];
bool visited[12][6] = {false};
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void solve_bfs (int x, int y, char color, vector<pair<int, int>> &pop) {
    queue<pair<int, int>> q;
    q.push({x, y});
    visited[x][y] = true;
    pop.push_back({x, y});
    
    while (!q.empty()) {
        auto [cx, cy] = q.front();
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int nx = cx + dx[i];
            int ny = cy + dy[i];
            if (nx < 0 || nx >= 12 || ny < 0 || ny >= 6) continue;
            
            if (!visited[nx][ny] && mapping[nx][ny] == color) {
                visited[nx][ny] = true;
                q.push({nx, ny});
                pop.push_back({nx, ny});
            }
        }
    }
}

bool puyo() {
    bool token = false;
    memset(visited, false, sizeof(visited));
    
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 6; j++) {
            if (mapping[i][j] != '.' && !visited[i][j]) {
                vector<pair<int, int>> pop;
                solve_bfs (i, j, mapping[i][j], pop);
                
                if (pop.size() >= 4) {
                    token = true;
                    
                    for (auto [x, y] : pop) {
                        mapping[x][y] = '.';
                    }
                }
            }
        }
    }
    
    return token;
}

void applyGravity() {
    for (int j = 0; j < 6; j++) {
        for (int i = 11; i >= 0; i--) { 
            if (mapping[i][j] == '.') { // 만약 터졌는데 점이 있으면
                for (int k = i - 1; k >= 0; k--) { // 밑에있는곳
                    if (mapping[k][j] != '.') {
                        swap(mapping[i][j], mapping[k][j]); // 위치 바꾸기
                        break;
                    }
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    for (int i = 0; i < 12; i++) {
        for (int j = 0; j < 6; j++) {
            cin >> mapping[i][j];
        }
    }
    
    int cnt = 0;
    while (true) {
        if (puyo()) {
            applyGravity();
            cnt++;
        } 
        
        else {
            break;
        }
    }
    
    cout << cnt << "\n";
    
    return 0;
}

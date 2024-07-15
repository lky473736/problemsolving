#include <bits/stdc++.h>
using namespace std;

const int GRID_SIZE = 5;
const int COMB_SIZE = 7;

// 방향 벡터: 상, 하, 좌, 우
const vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

// BFS를 사용하여 연결 여부 확인
bool is_connected_bfs(const vector<pair<int, int>>& indices, const vector<vector<char>>& grid) {
    vector<vector<bool>> visited(GRID_SIZE, vector<bool>(GRID_SIZE, false));
    queue<pair<int, int>> q;
    q.push(indices[0]);
    visited[indices[0].first][indices[0].second] = true;
    
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        
        for (auto [dx, dy] : directions) {
            int nx = x + dx;
            int ny = y + dy;
            if (nx >= 0 && nx < GRID_SIZE && ny >= 0 && ny < GRID_SIZE &&
                !visited[nx][ny] && find(indices.begin(), indices.end(), make_pair(nx, ny)) != indices.end() &&
                (grid[nx][ny] == 'S' || grid[nx][ny] == 'Y')) {
                visited[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
    
    // 모든 인덱스가 방문되었는지 확인
    for (const auto& index : indices) {
        if (!visited[index.first][index.second]) {
            return false;
        }
    }
    
    return true;
}

int main() {
    vector<vector<char>> grid(GRID_SIZE, vector<char>(GRID_SIZE));
    
    // 5x5 배열 입력 받기
    for (int i = 0; i < GRID_SIZE; ++i) {
        for (int j = 0; j < GRID_SIZE; ++j) {
            cin >> grid[i][j];
        }
    }
    
    // 모든 가능한 조합 생성
    vector<pair<int, int>> all_positions;
    for (int i = 0; i < GRID_SIZE; ++i) {
        for (int j = 0; j < GRID_SIZE; ++j) {
            all_positions.push_back({i, j});
        }
    }
    
    int cnt = 0;
    
    // 모든 조합 중에서 7개의 인덱스 조합을 생성하고 검사
    for (int i1 = 0; i1 < GRID_SIZE * GRID_SIZE; ++i1) {
        for (int i2 = i1 + 1; i2 < GRID_SIZE * GRID_SIZE; ++i2) {
            for (int i3 = i2 + 1; i3 < GRID_SIZE * GRID_SIZE; ++i3) {
                for (int i4 = i3 + 1; i4 < GRID_SIZE * GRID_SIZE; ++i4) {
                    for (int i5 = i4 + 1; i5 < GRID_SIZE * GRID_SIZE; ++i5) {
                        for (int i6 = i5 + 1; i6 < GRID_SIZE * GRID_SIZE; ++i6) {
                            for (int i7 = i6 + 1; i7 < GRID_SIZE * GRID_SIZE; ++i7) {
                                vector<pair<int, int>> indices = {
                                    all_positions[i1], all_positions[i2], all_positions[i3],
                                    all_positions[i4], all_positions[i5], all_positions[i6],
                                    all_positions[i7]
                                };
                                
                                if (is_connected_bfs(indices, grid)) {
                                    int countS = 0;
                                    int countY = 0;
                                    for (const auto& index : indices) {
                                        if (grid[index.first][index.second] == 'S') {
                                            countS++;
                                        } else if (grid[index.first][index.second] == 'Y') {
                                            countY++;
                                        }
                                    }
                                    if (countY < countS) {
                                        cnt++;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    
    cout << cnt;
    
    return 0;
}
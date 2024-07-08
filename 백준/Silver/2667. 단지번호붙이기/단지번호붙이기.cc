#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int N;
vector<vector<char>> map;
vector<vector<bool>> visited;

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int bfs(int startX, int startY) {
    queue<pair<int, int>> q;
    q.push({startX, startY});
    visited[startX][startY] = true;
    int count = 1;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && map[nx][ny] == '1') {
                q.push({nx, ny});
                visited[nx][ny] = true;
                count++;
            }
        }
    }
    
    return count;
}

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);
    
    cin >> N;

    map.resize(N, vector<char>(N));
    visited.resize(N, vector<bool>(N, false));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> map[i][j];
        }
    }

    vector<int> complexes;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (map[i][j] == '1' && !visited[i][j]) {
                int cnt = bfs(i, j);
                complexes.push_back(cnt);
            }
        }
    }

    sort(complexes.begin(), complexes.end());
    cout << complexes.size() << '\n';
    for (int count : complexes) {
        cout << count << '\n';
    }

    return 0;
}
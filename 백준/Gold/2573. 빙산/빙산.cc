#include <bits/stdc++.h>
using namespace std;

int N, M;
int arr[301][301];
int temp[301][301];
bool visited[1001][1001]; 
int dx[] = {0, 1, 0, -1};
int dy[] = {-1, 0, 1, 0};

void melting_ice () {
    for (int x = 1; x <= N; x++)
        for (int y = 1; y <= M; y++) {
            temp[x][y] = arr[x][y];
            
            if (temp[x][y] > 0) {
                for (int d = 0; d < 4; ++d) {
                    int nx = x + dx[d];
                    int ny = y + dy[d]; 
                    
                    if (1 <= nx && nx <= N && 1 <= ny && ny <= M && arr[nx][ny] == 0) { // dfs
                        temp[x][y] -= 1;
                    }
                }
                
                if (temp[x][y] < 0) { // 주변에 있는 얼음으로 인하여 이미 녹았으면
                    temp[x][y] = 0;
                }
            }
        }
        
    for (int x = 1; x <= N; x++) {
        for(int y = 1; y <= M; y++) {
            arr[x][y] = temp[x][y];
        }
    }
}

bool solve_bfs() {
    memset(visited, false, sizeof(visited)); // 초기화
    int mountain = 0;
    queue<pair<int, int>> q;
    
    for (int n = 1; n <= N; n++) {
        for (int m = 1; m <= M; m++) {
            if (!visited[n][m] && arr[n][m] > 0) { // 방문한 적 없고 얼음이 아직 있다면 
                if(++mountain > 1) { // 빙산 2개 이상
                    return true;
                }
                
                q.push(make_pair(n, m));
                visited[n][m] = true;
                
                while (!q.empty()) { // bfs
                    auto tec = q.front(); 
                    q.pop();
                    
                    int x = tec.first;
                    int y = tec.second;
                    
                    for (int d = 0; d < 4; ++d){
                        int nx = x + dx[d];
                        int ny = y + dy[d]; 
                        
                        if (1 <= nx && nx <= N && 1 <= ny && ny <= M) { 
                            if (!visited[nx][ny] && arr[nx][ny] > 0) {
                                visited[nx][ny] = true;
                                q.push(make_pair(nx, ny));
                            }
                        }
                    }
                }
            }
        }
    }
    
    return false; // 만약 아무것도 하지 못하였다면
}

// ********
int checking_empty () { // 얼음이 다 녹았는지 안녹았는지 체크
    for (int n = 1; n <= N; ++n) {
        for (int m = 1; m <= M; ++m) {
            if (arr[n][m] > 0) {  // 만약 얼음이 있으면
                return 1;
            }
        }
    }
    
    return 2; // 없으면
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;
    
    for (int n = 1; n <= N; n++) {
        for (int m = 1; m <= M; m++) {
            cin >> arr[n][m];
        }
    }
    
    int rst = 1;
    
    while (true){
        melting_ice(); // 녹기
        
        bool token = solve_bfs();
        
        if (solve_bfs() == true) {
            break;
        }
        
        else {
            if (checking_empty() != 1) { 
                rst = 0;
                break;
            }
        }
        
        rst++;
    }
    
    cout << rst;
    return 0;
}
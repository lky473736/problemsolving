// #include <bits/stdc++.h>
// using namespace std;

// int k, h, w;
// int field[201][201];
// int chance[201][201][31] = {0};
// int visited[201][201][31] = {0};

// // 기본 이동
// int dx[] = {-1, 0, 1, 0};
// int dy[] = {0, 1, 0, -1};

// // 말 이동
// int hx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
// int hy[] = {1, 2, 2, 1, -1, -2, -2, -1};

// /*
// { -2,-1,1,2,2,1,-1,-2 };
// { 1,2,2,1,-1,-2,-2,-1 };
// */
 
// void solve_bfs() {
//     queue <tuple<int, int, int>> q; // 3차원
//     q.push(make_tuple(0, 0, 0));
//     visited[0][0][0] = 1;
    
//     while (!q.empty()) {
//         int x, y, k;
//         tie(x, y, k) = q.front(); // q.front 넣어줌
//         q.pop();
        
//         for (int i = 0; i < 4; i++) { // 그냥 이동
//             int nx = x + dx[i];
//             int ny = y + dy[i];
            
//             if ((0 <= nx && nx < h) && (0 <= ny && ny < w) && field[nx][ny] != 1) {  
//                 if (visited[nx][ny][k] == 0) {
//                     visited[nx][ny][k] = 1; // 이동
//                     chance[nx][ny][k] = chance[x][y][k] + 1;
//                     q.push(make_tuple(nx, ny, k));
//                 }
//             }
//         }
        
//         // 그냥 이동 후에 말의 이동까지 고려해보아야 함 (더 빨리 갈 수 있으니깐)
        
//         for (int i = 0; i < 8; i++) { // 말의 이동
//             int nx = x + hx[i];
//             int ny = y + hy[i];
            
//             if ((0 <= nx && nx < h) && (0 <= ny && ny < w) && k + 1 <= k) {
//                 if (visited[nx][ny][k + 1] == 0 && field[nx][ny] != 1) {
//                     visited[nx][ny][k + 1] = 1; // 이동
//                     chance[nx][ny][k + 1] = chance[x][y][k] + 1; // 경우의 수 늘리기
//                     q.push(make_tuple(nx, ny, k + 1));
//                 } 
//             }
//         }
//     }
// }
 
// int main() {
//     ios::sync_with_stdio (0);
//     cin.tie(0);
    
//     cin >> k;
//     cin >> w >> h;
    
//     for (int i = 0; i < h; i++) {
//         for (int j = 0; j < w; j++) {
//             cin >> field[i][j];
//         }
//     }
    
//     solve_bfs();
    
//     int rst = 1000000;
//     bool token = false;
    
//     for (int i = 0; i < k + 1; i++) {
//         if (chance[h-1][w-1][i] == 0 && visited[h-1][w-1][i] == 0) { // 이런 경우가 없다면
//             continue;
//         }
        
//         token = true;
//         rst = min(rst, chance[h-1][w-1][i]); // 경우 중 가장 최소를 골라라
//     }
    
//     if (token == false) {
//         cout << -1;
//     }
    
//     else {
//         cout << rst;
//     }

//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int k, h, w;
int field[201][201];
int chance[201][201][31] = {0};
int visited[201][201][31] = {0};

// 기본 이동
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, 1, 0, -1};

// 말 이동
int hx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
int hy[] = {1, 2, 2, 1, -1, -2, -2, -1};

void solve_bfs() {
    queue<tuple<int, int, int>> q; // 3차원
    q.push(make_tuple(0, 0, 0));
    visited[0][0][0] = 1;
    
    while (!q.empty()) {
         // 시작점 방문 처리
        int x, y, curr_k;
        tie(x, y, curr_k) = q.front();
        q.pop();
        
        for (int i = 0; i < 4; i++) { // 기본 이동
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            // 이동 가능한 범위 내에 있고, 장애물이 없으며, 아직 방문하지 않은 경우
            if (nx >= 0 && nx < h && ny >= 0 && ny < w && field[nx][ny] != 1) {  
                if (visited[nx][ny][curr_k] == 0) {
                    visited[nx][ny][curr_k] = 1;
                    chance[nx][ny][curr_k] = chance[x][y][curr_k] + 1; // 방문 추가
                    q.push(make_tuple(nx, ny, curr_k));
                }
            }
        }
        
        for (int i = 0; i < 8; i++) { // 말의 이동
            int nx = x + hx[i];
            int ny = y + hy[i];
            
            // 이동 가능한 범위 내에 있고, 말 이동 횟수 제한 내이며, 아직 방문하지 않은 경우
            if (nx >= 0 && nx < h && ny >= 0 && ny < w && curr_k + 1 <= k) {
                if (visited[nx][ny][curr_k + 1] == 0 && field[nx][ny] != 1) {
                    visited[nx][ny][curr_k + 1] = 1;
                    chance[nx][ny][curr_k + 1] = chance[x][y][curr_k] + 1; // 방문 추가
                    q.push(make_tuple(nx, ny, curr_k + 1));
                } 
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> k;
    cin >> w >> h;
    
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cin >> field[i][j];
        }
    }
    
    solve_bfs();
    
    int rst = INT_MAX; 
    bool token = false;
    
    // 모든 경우의 수 탐색
    for (int i = 0; i < k + 1; i++) {
        if (chance[h-1][w-1][i] == 0 && visited[h-1][w-1][i] == 0) {
            continue;
        }
        
        else {
            // token = false;
            token = true; // 도착지 도달함
            rst = min(rst, chance[h-1][w-1][i]); // 최소 경우의 수 갱신
        }
    }
    
    if (token == false) {
        cout << -1; 
    } 
    
    else {
        cout << rst;
    }

    return 0;
}
#include <bits/stdc++.h>
using namespace std;

/*
    일단 끝까지 움직인다 
        -> 장애물 만났다 -> 그만
        -> 벽 만났다 -> 그만
    겹친다 -> blue와 red의 선후관계 보기
*/

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

struct state {
    int rx, ry, bx, by, cnt;
    // rx : 빨간공 x, ry : 빨간공 y
    // bx : 파란공 x, by : 파란공 y
};

void move (int &x, int &y, int dx, int dy, const vector<vector<char>> &board) {
    while (board[x + dx][y + dy] != '#' && board[x][y] != 'O') { // 벽이 아니거나 홀이 아니라면
        x += dx; // 끝까지 이동시키고 봄
        y += dy;
    }
}

int solve_bfs (vector<vector<char>> &board, int rx, int ry, int bx, int by) {
    // int n = board.size();
    // int m = board[0].size();
    
    queue<state> q;
    q.push({rx, ry, bx, by, 0});
    
    set<vector<int>> visited;
    visited.insert({rx, ry, bx, by});

    while (!q.empty()) {
        state current = q.front(); // 현재 위치 구조체
        q.pop();

        if (current.cnt >= 10) { // 10 제한
            return -1;
        }

        for (int i = 0; i < 4; i++) {
            int nrx = current.rx, nry = current.ry; // 큐 맨 앞 rx, ry
            int nbx = current.bx, nby = current.by; // 큐 맨 앞 bx, by

            move(nrx, nry, dx[i], dy[i], board); // red 움직이고
            move(nbx, nby, dx[i], dy[i], board); // blue 움직이고

            if (board[nbx][nby] == 'O') { // b가 홀 만나면
                continue;
            } 
            if (board[nrx][nry] == 'O') { 
                return current.cnt + 1; // r이 홀 만나면 종료
            }

            if (nrx == nbx && nry == nby) { // red랑 blue가 같으면
                if (abs(nrx - current.rx) + abs(nry - current.ry) > abs(nbx - current.bx) + abs(nby - current.by)) {
                    nrx -= dx[i];
                    nry -= dy[i];
                }  // blue가 red보다 빠르면 
                
                else {
                    nbx -= dx[i];
                    nby -= dy[i];
                } // red가 blue보다 빠르면
            }

            // 현재 위치가 visited set의 끝에 놓여져 있다면
            if (visited.find({nrx, nry, nbx, nby}) == visited.end()) {
                visited.insert({nrx, nry, nbx, nby}); 
                q.push({nrx, nry, nbx, nby, current.cnt + 1}); // 이동 횟수 1 증가
            }
        }
    }

    return -1; // 아무것도 안되면
}

int main() {
    int N, M;
    cin >> N >> M;
    
    vector<vector<char>> board(N, vector<char>(M)); // board
    int rx, ry, bx, by;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            cin >> board[i][j];
            
            // r 위치
            if (board[i][j] == 'R') { 
                rx = i;
                ry = j;
            } 
            
            // b 위치
            else if (board[i][j] == 'B') {
                bx = i;
                by = j;
            }
        }
    }

    int rst = solve_bfs (board, rx, ry, bx, by);
    
    cout << rst << endl;

    return 0;
}

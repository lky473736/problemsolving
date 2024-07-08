#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

int N = 0;

int map[101][101];
bool visited[101][101];

int dx[4] = {0, 1, 0, -1};
int dy[4] = {-1, 0, 1, 0};

void dfs (int px, int py, int num) { // find the edge that is posited the end
	int x = 0, y = 0;

	map[px][py] = num;
	visited[px][py] = true;

	for (int i = 0; i < 4; i++) { // four directions
		x = px + dx[i];
		y = py + dy[i];
		
		if (x >= 0 && x < N && y >= 0 && y < N) {
			if (map[x][y] != 0) { 
			    if (!visited[x][y]) {
			        visited[x][y] = true;
				    dfs(x, y, num);
			    }
			}
		}
	}
	
	return;
}

int bfs (int num) { // union found
	queue<pair<int, int>> q;
	int px, py, x, y;
	int dist = 0; 
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (map[i][j] == num) { 
				q.push(make_pair(i, j));
				visited[i][j] = true;
			}
		}
	}

	while (!q.empty()) {
		int size = q.size();
		
		for (int i = 0; i < size; i++) {
			px = q.front().first;
			py = q.front().second;
			q.pop();

			for (int j = 0; j < 4; j++) {
				x = px + dx[j];
				y = py + dy[j];
				
				if (x >= 0 && x < N && y >= 0 && y < N) {
					if (map[x][y] != 0 && map[x][y] != num) {
						return dist;
					}
					
					if (map[x][y] == 0 && !visited[x][y]) { 
						visited[x][y] = true;
						q.push(make_pair(x, y));
					}
				}
			}
		}
		
		dist += 1;
	}
	
	return dist;
}

int main() {
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
			
			if (map[i][j] == 1) {
			    map[i][j] = -1; // division the continents
			}
		}
	}

	int num = 1;
	for (int i = 0; i < N; i++) { 
		for (int j = 0; j < N; j++) {
			if (map[i][j] == -1 && !visited[i][j]) {
				dfs (i, j, num);
				num += 1;
			}
		}
	}

	int rst = NULL;
	for (int i = 1; i < num; i++) {
        memset(visited, false, sizeof(visited));

        int distance = bfs(i);

        if (rst == NULL || distance < rst) {
            rst = distance;
        }
    }
	
	cout << rst << "\n";
}
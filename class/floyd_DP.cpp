#include <bits/stdc++.h>
#include <climits>

using namespace std;

const int INF = INT_MAX;

// Floyd-Warshall using DP
void floyd(int n, vector<vector<int>>& W, vector<vector<int>>& D) {
    D = W;

    for (int k = 0; k < n; k++) {      
        for (int i = 0; i < n; i++) {    
            for (int j = 0; j < n; j++) { 
                if (D[i][k] != INF && D[k][j] != INF)
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
            }
        }
    }
}

void printMatrix(const vector<vector<int>>& mat) {
    for (const auto& row : mat) {
        for (int val : row) {
            if (val == INF) cout << "INF ";
            else cout << val << " ";
        }
        cout << '\n';
    }
}

int main() {
    int n = 4;

    vector<vector<int>> W = {
        {0,   3,   INF, 5},
        {2,   0,   INF, 4},
        {INF, 1,   0,   INF},
        {INF, INF, 2,   0}
    };

    vector<vector<int>> D(n, vector<int>(n, INF));

    floyd(n, W, D);

    cout << "최단 거리 행렬 D:" << endl;
    printMatrix(D);

    return 0;
}

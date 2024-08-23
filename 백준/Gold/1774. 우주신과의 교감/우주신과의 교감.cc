#include <bits/stdc++.h>
using namespace std;

double rst; // 총 가중치
vector<pair<int, int>> mapping; // map
vector<vector<double>> edges; // 간선
int parent[100000]; // 부모 노드 (처음에는 -1로 초기화할거임)

int compare (const vector<double>& a, const vector<double>& b) {
    return a[2] < b[2];  // 거리가 작은 순대로
}

double dist (int i, int j) { // euclidean distance
    long long x_c = pow(mapping[i].first - mapping[j].first, 2);
    long long y_c = pow(mapping[i].second - mapping[j].second, 2);
    
    return sqrt(x_c + y_c);
}

int find (int x) { // x의 루트 찾기 (경로압축)
    if (parent[x] < 0) {
        return x;
    }
    
    return parent[x] = find(parent[x]);
}

void unionf (int x, int y) {
    x = find(x); // 루트 찾고
    y = find(y); // 루트 찾고

    if (x != y) {
        if (parent[x] < parent[y]) { 
            parent[x] += parent[y];
            parent[y] = x;
        } 
        
        else {
            parent[y] += parent[x];
            parent[x] = y;
        }
    }
}

void kruskal() {
    for (const auto& edge : edges) {
        int u = edge[0];
        int v = edge[1];
        double weight = edge[2];

        if (find(u) != find(v)) {
            unionf(u, v);
            rst += weight;
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    fill(parent, parent + 100000, -1); // 처음에는 -1로 초기화

    for (int i = 0; i < n; ++i) {
        int x, y;
        cin >> x >> y;
        
        mapping.push_back(make_pair(x, y)); // https://velog.io/@ehdbs28/emplaceback-%EA%B3%BC-pushback%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90
    }

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            edges.push_back({(double)i, (double)j, dist(i, j)});
            // 간선 추가 : (i, j, 거리)
        }
    }

    sort (edges.begin(), edges.end(), compare); // https://velog.io/@ehdbs28/C-STL-%EC%A0%95%EB%A0%ACSort-%ED%95%A8%EC%88%98

    for (int i = 0; i < m; ++i) {
        int x, y;
        cin >> x >> y;
        
        unionf(x - 1, y - 1);
    }

    kruskal();
    cout << fixed << setprecision(2) << rst << "\n";

    return 0;
}
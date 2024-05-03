#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
#include <memory.h>

int adjacent_matrix[1001][1001]; // adjacent matrix
int visited[1001];
int queue[1001]; // visited, queue
 
void DFS(int N, int V);
void BFS(int N, int V);
 
int main() {
	int N, M, V;
	scanf ("%d %d %d", &N, &M, &V);
 
	int x, y;
	for (int i = 0; i < M; i++) { // make the adjacent matrix
		scanf("%d %d", &x, &y);
		adjacent_matrix[x][y] = 1;
		adjacent_matrix[y][x] = 1;
	}
 
	DFS (N, V); 
	printf ("\n");
	memset(visited, 0, sizeof(int) * (N + 1)); 
	// memory setting to 0 (initialization)
	
	BFS (N, V);
	return 0;
}
 
void DFS(int N, int V) {
	visited[V] = 1; // set 1 due to express the visited sign
	printf("%d ", V);
	
	for (int i = 0; i < N; i++) {
		if (visited[i+1] == 0 && adjacent_matrix[V][i+1] == 1) {
		    // if not visited and related on specific position of adjacent matrix
			DFS(N, i+1);
		}
	}
	
	return;
}
 
void BFS(int N, int V) {
	int front = -1, rear = 0, pop_ind = 0;
	printf("%d ", V);
	visited[V] = 1;
	queue[0] = V;
 
	while (front < rear) {
		pop_ind = queue[++front];
		
		for (int i = 0; i < N; i++) {
			if (visited[i+1] == 0 && adjacent_matrix[pop_ind][i+1] == 1) {
				printf("%d ", i+1);
				
				visited[i+1] = 1; 
				queue[++rear] = i+1;
			}
		}
	}
	return;
}
#include <bits/stdc++.h>
#include <time.h>
using namespace std;

int S[] = {1, 4, 2, 5, 10, 9, 3};

// merge sort using recursion (divide and conquer)
void merge(int h, int m, int* U, int* V, int* S) {
    int i = 0, j = 0, k = 0;  // 인덱스 0부터 시작

    while (i < h && j < m) {
        if (U[i] < V[j]) { 
            S[k++] = U[i++];
        } else {
            S[k++] = V[j++];
        }
    }
    
    // 남은 요소 복사
    while (i < h) S[k++] = U[i++];
    while (j < m) S[k++] = V[j++];
}

void merge_sort(int *S, int n) {
    if (n > 1) {
        int h = n / 2; // 왼쪽 크기
        int m = n - h; // 오른쪽 크기

        int U[h], V[m];

        for (int i = 0; i < h; i++) U[i] = S[i];      // 왼쪽 복사
        for (int i = 0; i < m; i++) V[i] = S[h + i];  // 오른쪽 복사

        merge_sort(U, h);
        merge_sort(V, m);
        merge(h, m, U, V, S);
    }
}

int main() {
    cout << "Before: ";
    for (int i = 0; i < 7; i++) cout << S[i] << ' ';
    cout << endl;
    
    clock_t start, end;
    
    start = clock();
    merge_sort(S, 7);
    end = clock();
    
    double result = (double)(end - start) / CLOCKS_PER_SEC * 1e9;  // ns 단위 변환
    
    cout << "After: ";
    for (int i = 0; i < 7; i++) cout << S[i] << ' ';
    cout << endl;
    cout << "Merge Sort Time: " << result << " ns" << endl;
}

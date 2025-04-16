#include <bits/stdc++.h>
using namespace std;

void merge(int h, int m, int* U, int* V, int* S) {
    int i = 0, j = 0, k = 0;
    while (i < h && j < m) {
        if (U[i] < V[j]) { S[k++] = U[i++]; }
        else { S[k++] = V[j++]; }
    }

    while (i < h) { S[k++] = U[i++]; }
    while (j < m) { S[k++] = V[j++]; }
}

void mergeSort(int n, int* S) {
    if (n > 1) {
        int h = n / 2;
        int m = n - h;
        int* U = new int[h];
        int* V = new int[m];

        // divide
        for (int i = 0; i < h; i++) { U[i] = S[i]; }
        for (int i = 0; i < m; i++) { V[i] = S[h + i]; }

        // conquer
        mergeSort(h, U);
        mergeSort(m, V);
        merge(h, m, U, V, S);

        delete[] U;
        delete[] V;
    }
}

int main() {
    cin.tie(0); ios::sync_with_stdio(0);
    int n; cin >> n;
    int *arr = new int[n];
    for (int i = 0; i < n; i++) { cin >> arr[i]; }
    mergeSort(n, arr);
    for (int i = n-1; i >= 0; i--) { cout << arr[i] << '\n'; }
    cout << endl;
}



/*
    void merge (int h, int m, int *U, int *V, int *S) {
        int i=1, j=1, k=1;
        while (i <= h && j <= m) {
            if (U[i] < V[j]) { S[k] = U[i]; i++; }
            else { S[k] = V[j]; j++; }
            k++;
        }
        
        if (i > h) { copy V[j:m] to S[k:h+m]; }
        else { copy U[i:h] to S[k:h+m]; }
    }
    
    void mergeSort (int n, int *S) {
        if (n>1) {
            int h = floor(n/2);
            int m = n-h;
            int U[1...h];
            int V[1...m];
            
            // divide
            copy S[1...h] to U[1...h];
            copy S[h+1...n] to V[1...m];
            
            // conquer
            mergeSort(h, U);
            mergeSort(m, V);
            merge (h, m, U, V, S);
        }
    }
*/
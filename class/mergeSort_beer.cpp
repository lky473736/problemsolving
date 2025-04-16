#include <bits/stdc++.h>
using namespace std;

int S[] = {1, 9, 2, 3, 4};
int N = 5; 
int call_num_1 = 0;
int call_num_2 = 0;

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

void merge (int h, int m, int *U, int *V, int *S) {
    // i for U, j for V, k for S 
    int i = 0, j = 0, k = 0;
    
    while (i < h && i < m) {
        if (U[i] < V[j]) {
            S[k] = U[i];
            i++;
        } else {
            S[k] = V[j];
            j++;
        }
        k++;
    }
    
    if (i > h) {
        while (j < m) { S[k++] = V[j++]; }
    } else {
        while (i < h) { S[k++] = U[i++]; }
    }
    
    cout << "call merge : " << ++call_num_2 << endl;
    cout << "U : ";
    for (int i = 0; i < h; i++) { cout << U[i] << ' '; }
    cout << endl;
    cout << "V : ";
    for (int i = 0; i < m; i++) { cout << V[i] << ' '; }
    cout << endl;
    cout << "S : ";
    for (int i = 0; i < N; i++) { cout << S[i] << ' '; }
    cout << endl;
    cout << endl;
}

void mergeSort(int n, int *arr) {
    if (n > 1) {
        int h = floor(n/2);
        int m = n-h;
        int *U = new int[h];
        int *V = new int[m];
        
        // divide
        for (int i = 0; i < h; i++) { U[i] = S[i]; }
        for (int i = 0; i < m; i++) { V[i] = S[i+h]; }
        
        cout << "call mergeSort : " << ++call_num_1 << endl;
        cout << "U : ";
        for (int i = 0; i < h; i++) { cout << U[i] << ' '; }
        cout << endl;
        cout << "V : ";
        for (int i = 0; i < m; i++) { cout << V[i] << ' '; }
        cout << endl;
        cout << endl;
        
        // conquer
        mergeSort(h, U);
        mergeSort(m, V);
        
        // combine
        merge (h, m, U, V, S);
    }
}

int main()
{
    mergeSort(5, S);
    for (int i = 0; i < 5; i++) { cout << S[i] << ' ';}
}

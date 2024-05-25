#include <stdio.h>

int main() {
    int arr[8][3] = {
        {4, 4, 7},
        {0, 0, 1},
        {0, 1, 10},
        {1, 0, 2},
        {2, 0, -1},
        {2, 1, -13},
        {2, 2, 1},
        {3, 3, -7}
    };
    
    int sparse_matrix[4][4];

    for (int i = 1; i < 8; i++) {
        sparse_matrix[arr[i][0]][arr[i][1]] = arr[i][2];
    }
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf ("%d ", sparse_matrix[i][j]);
        }
        
        putchar ('\n');
    }
    
    return 0;
}

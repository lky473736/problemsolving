#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    int rst[2];
    int x[3], y[3];
    int tx = 0;
    int ty = 0;
    int cx[2][2] = {0, 0, 0, 0};
    int cy[2][2] = {0, 0, 0, 0};
    
    for (int i = 0; i < 3; i++) {
        int px, py;
        scanf ("%d %d", &px, &py);
        
        if (tx == 0 && px != x[i-1] && i != 0) {
            cx[0][0] = px;
            cx[1][0] = x[i-1];
            tx = 1;
        }
        
        if (ty == 0 && py != y[i-1] && i != 0) {
            cy[0][0] = py;
            cy[1][0] = y[i-1];
            ty = 1;
        }
        
        x[i] = px;
        y[i] = py;
    }
    
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            if (x[j] == cx[i][0]) {
                cx[i][1] += 1;
            }
        }
        
        for (int j = 0; j < 3; j++) {
            if (y[j] == cy[i][0]) {
                cy[i][1] += 1;
            }
        }
    }
    
    // for (int i = 0; i < 2; i++) {
    //     printf ("cx : %d %d\n", cx[i][0], cx[i][1]);
    //     printf ("cy : %d %d\n", cy[i][0], cy[i][1]);
    // }
    
    for (int i = 0; i < 2; i++) {
        if (cx[i][1] == 1) {
            printf ("%d ", cx[i][0]);
            break;
        }
    }
    
    for (int i = 0; i < 2; i++) {
        if (cy[i][1] == 1) {
            printf ("%d ", cy[i][0]);
            break;
        }
    }
    
    return 0;
}
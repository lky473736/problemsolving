#include <iostream>
#include <cstdio>
#include <map>
#include <unistd.h>

int main() {
    int arr[10][10];
    int position_food[2];
    
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            scanf ("%d", arr[i]+j);
            
            if (arr[i][j] == 2) {
                position_food[0] = i;
                position_food[1] = j;
            }
        }
    }
    
    int ant_r = 1, ant_c = 1;
    
    if (arr[ant_r][ant_c] == 2) {
        arr[ant_r][ant_c] = 9;
        goto k;
    }
    
    arr[ant_r][ant_c] = 9;
    
    // printf ("%d %d\n", position_food[0], position_food[1]);
    
    for (int i = 0; i < 50; i++) {
        // printf ("%d %d\n", ant_r, ant_c);
        // printf ("%d %d\n", distance_r, distance_c);
        // printf ("----------\n");
        // sleep(1);

        if (arr[ant_r][ant_c+1] != 1) {
            ant_c += 1;
        }
        
        else {
            ant_r += 1;
        }
        
        if (ant_r == position_food[0] and ant_c == position_food[1]) {
            arr[ant_r][ant_c] = 9;
            break;
        }
        
        if (arr[ant_r][ant_c] != 1 or arr[ant_r][ant_c] != 1) {
            arr[ant_r][ant_c] = 9;
        }
        
        else {
            break;
        }
    }
    
k:
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            printf ("%d ", arr[i][j]);
        }
        
        printf ("\n");
    }
    
    return 0;
}

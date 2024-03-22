#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int find_win (char a, char b);

int main() {
    int t = 0; 
    scanf ("%d", &t);
    
    for (int i = 0; i < t; i++) {
        int n = 0;
        scanf ("%d", &n);
        
        int w1 = 0, w2 = 0;
        
        for (int j = 0; j < n; j++) {
            char p1, p2;
            scanf(" %c %c", &p1, &p2);
            // int _ = getchar(); // 버퍼처리

            // printf ("%d\n", find_win(p1, p2));
            
            switch(find_win(p1, p2)) {
                case 1 :
                    w1++;
                    continue;
                    
                case 0 :
                    continue;
                    
                case -1 :
                    w2++;
                    continue;
                    
                default :
                    continue;
            }
        }
        
        // printf ("%d %d\n", w1, w2);
        
        if (w1 == w2) {
            printf ("TIE\n");
        }
        
        else {
            if (w1 > w2) {
                printf ("Player 1\n");
            }
            
            else {
                printf ("Player 2\n");
            }
        }
    }
    
    return 0;
}

int find_win(char a, char b) {
    if (a == 'R') {
        switch (b) {
            case 'R':
                return 0;

            case 'P':
                return -1;

            case 'S':
                return 1;

            default:
                return -2;
        }
    } else if (a == 'S') {
        switch (b) {
            case 'R':
                return -1;

            case 'P':
                return 1;

            case 'S':
                return 0;

            default:
                return -2;
        }
    } else { // P
        switch (b) {
            case 'R':
                return 1;

            case 'P':
                return 0;

            case 'S':
                return -1;

            default:
                return -2;
        }
    }
}
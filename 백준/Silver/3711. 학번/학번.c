#include <stdio.h>
#include <stdbool.h>

int main()
{
    int N;
    
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++) {
        int G, arr[300];
        
        scanf ("%d", &G);
        
        if (G != 1) {
            for (int j = 0; j < G; j++) {
                int id;
                scanf ("%d", &id);
                arr[j] = id;
            }
            
            int l = 1;
            
            while (true) {
                l = l + 1;
                
                int rest[300];
                int token = 0;
                
                for (int k = 0; k < G; k++) {
                    rest[k] = arr[k] % l;
                    
                    for (int x = 0; x < k+1; x++) {
                        if (rest[x] == arr[k] % l && x != k) {
                            token = 1;
                            break;
                        }
                    }
                    
                    if (token == 1) {
                        break;
                    }
                }
                
                if (token == 1) {
                    ;
                }
                
                else {
                    break;
                }
            }
            
            printf ("%d\n", l);
        }
        else {
            int s = 0;
            scanf ("%d", &s);
            
            printf ("1\n");
        }
    }
    
    return 0;
}
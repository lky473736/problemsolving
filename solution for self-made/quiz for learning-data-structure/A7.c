#include <stdio.h>
#include <stdbool.h>
#define MAX_POSITION_NAME 3

int radix_arr_1[10][10];
int radix_arr_10[10][10];
int radix_arr_100[10][10];
int arr[] = {1, 100, 32, 8, 299, 832, 18, 19, 72, 256};

int main()
{
    int (*address[3])[10] = {radix_arr_1, radix_arr_10, radix_arr_100};
    int queue[] = {1, 100, 32, 8, 299, 832, 18, 19, 72, 256};
    int mv = 0;
    
    for (int i = 0; i < MAX_POSITION_NAME; i++) {
        mv = 0;
        int (*current_address)[10] = address[i];
        
        for (int j = 0; j < 10; j++) {
            int posi_100 = queue[j] / 100;
            int posi_10 = (queue[j] % 100) / 10;
            int posi_1 = (queue[j] % 10) / 1;
            
            int posi_num[3] = {posi_1, posi_10, posi_100};
            
            while (true) {
                if (current_address[posi_num[i]][mv] == 0){
                    current_address[posi_num[i]][mv] = queue[j];
                    break;
                }
                else {
                    mv++;
                }
            }
        }
        
        mv = 0;
        
        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                if (current_address[j][k] != 0) {
                    queue[mv++] = current_address[j][k];
                    printf ("%d ", current_address[j][k]);
                    current_address[j][k] = 0;
                }
            }
        }
        
        printf ("\n");
    }

    return 0;
}

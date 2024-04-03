#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int main() {
    int k, sum1 = 0, j = 0;
    scanf("%d", &k);
    
    int* number;
    number = (int*)malloc(sizeof(int) * k);
    
    int counting = 0;
    
    for (int i = 0; i < k; i++) {
        int input;
        scanf("%d", &input);
        
        if (input == 0) {
            number[counting-1] = 0;
            counting -= 1;
        }
        
        else {
            number[counting] = input;
            counting++;
        }
    }
    
    int p = 0;

    while (true) {
        if (number[p] == 0) {
            break;
        }
        
        sum1 += number[p];
        p += 1;
    }
    
    printf("%d\n", sum1);
    
    return 0;
}
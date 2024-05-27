#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// queue와 정렬을 이용한다. 정렬은 selection sort를 이용하였다.
// 편의 상 프로세스의 이름은 정수로 받는 것으로 한다.

int main() {
    int process_counting = 0;
    scanf ("%d", &process_counting);
    
    // process 배열 : {process 이름, process의 CPU 사용량}
    int** process = (int**) malloc(sizeof(int*) * process_counting);
    for (int i = 0; i < process_counting; i++) { 
        process[i] = (int*) malloc(sizeof(int) * 2); 
    } 
    
    int *queue[4];
    int *delete_process[4];
    int delete_num = 0;
    int head = 0, tail = 0;
    
    // queue
    for (int i = 0; i < process_counting; i++) {
        int process_name, process_cpu_use;
        scanf ("%d %d", process[i], process[i]+1);
        queue[tail] = process[i];
        
        if (i == 0) {
            ;
        }
        
        else {
            if (queue[tail][1] < queue[tail-1][1]) {
                delete_process[delete_num++] = queue[head];
                queue[head] = 0;
                head++;
            }
        }
        
        tail++;
    }
    
    // selection sort
    for (int i = 0; i < delete_num-1; i++) {
        for (int j = i+1; j <= delete_num-1; j++) {
            if (delete_process[i][1] > delete_process[j][1]) {
                int *temp = delete_process[i];
                delete_process[i] = delete_process[j];
                delete_process[j] = temp;
            }
        }
    }
    
    for (int i = 0; i < delete_num; i++) {
        printf ("%d\n", delete_process[i][0]);
    }
    
    return 0;
}

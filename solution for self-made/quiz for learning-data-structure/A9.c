#include <stdio.h>
#include <stdbool.h>
#define ARRAY_NUM 17

// 언제나 binary search가 빠른 건 아니다.

int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17};
int linear_count = 0;
int binary_count = 0;

int linear_search (int data) {
    for (int i = 0; i < ARRAY_NUM; i++) {
        linear_count++;
        
        if (arr[i] == data) {
            return i;
        }
    }
    
    return -1;
}

int binary_search (int data) {
    int start = 0;
    int end = ARRAY_NUM;
    int mid;

    while (true) {
        binary_count++;
        
        mid = (start + end) / 2;
        
        if (arr[mid] == data) {
            return mid;
        }
        
        else {
            if (arr[mid] < data) {
                start = mid + 1;
            }
            
            else {
                end = mid - 1;
            }
        }
    }
    
    return -1;
}

int main() {
    int position_linear = linear_search(2);
    int position_binary = binary_search(2);
    
    printf ("%d %d", linear_count, binary_count);
    
    return 0;
}

#include <stdio.h>

int main() {

    int i= 0, j= 0, N, arr[100];
    scanf_s("%d", &N);


    do {
        scanf_s("%d", &arr[i]);
        i++;
    } while (i < N);

    do {
        printf("%x ", arr[j]);
        j++;
    } while (j < N);

    return 0;

}

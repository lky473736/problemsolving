#include <stdio.h>

int main() {
    int decimal;
    printf("10진수를 입력하세요: ");
    scanf("%d", &decimal);

    int binary[32]; 
    int i = 0;

    if (decimal == 0) {
        binary[i] = 0;
        i++;
    } else {
        while (decimal > 0) {
            binary[i] = decimal % 2;
            decimal /= 2;
            i++;
        }
    }

    printf("2진수: ");
    if (i == 0) {
        printf("0");
    } else {
        for (int j = i - 1; j >= 0; j--) {
            printf("%d", binary[j]);
        }
    }
    printf("\n");

    return 0;
}

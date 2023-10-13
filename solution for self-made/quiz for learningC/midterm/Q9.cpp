#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
    char a[1000], b[2];
    int p, o = 0, i;

    printf("100 이상의 숫자를 입력하시오 : ");
    scanf("%s", a);

    p = strlen(a);

    if (p < 2) {
        printf("올바른 입력이 아닙니다. 최소 2자리 숫자를 입력하세요.\n");
        return 1;
    }

    while (p == 2) {
        p -= 1;
        o += 1;
    }

    i = (int)o;

    b[0] = a[o];
    b[1] = a[o + 1];

    int number = atoi(b); 
    int number1 = atoi(a);

    if (number % 4 == 0) {
        printf("%x", number1); 
    }
    else {
        printf("%o", number1);
    }

    return 0;
}

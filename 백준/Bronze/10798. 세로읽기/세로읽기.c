#include <stdio.h>
#include <string.h>

int main() {
    char S[7][17];
    int lenbig = 0;

    // 단어 길이 초기화
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 15; j++) {
            S[i][j] = '\0'; // '\0'으로 초기화하여 문자열의 끝을 표시
        }
    }

    // 단어 입력 및 최대 길이 계산
    for (int i = 0; i < 5; i++) {
        scanf("%s", S[i]);
        int curLen = strlen(S[i]);
        if (curLen > lenbig) {
            lenbig = curLen;
        }
    }

    // 세로로 읽어서 출력
    for (int i = 0; i < lenbig; i++) {
        for (int j = 0; j < 5; j++) {
            if (S[j][i] != '\0') { // '\0'이 아닌 경우에만 출력
                printf("%c", S[j][i]);
            }
        }
    }

    return 0;
}
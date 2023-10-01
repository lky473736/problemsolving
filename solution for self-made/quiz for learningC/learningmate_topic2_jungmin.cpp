/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 2 - 섭씨온도, 화씨온도 변환 (문정민)
  */

// 섭씨 온도 혹은 화씨 온도를 입력받아 섭씨 온도를 받았다면 화씨온도로, 화씨온도를 받았다면 섭씨온도로 변환시키는 코드를 입력하시오.
// 화씨 = (섭씨 * 9 / 5) + 32;
// 섭씨 = (화씨 - 32) * 5 / 9;


#include <stdio.h>

int main() {
    char tem;
    float c, f;

    printf("온도 단위를 입력하세요 (c 또는 f): ");
    scanf_s("%c", &tem);

    if (tem == 'c') {
        printf("섭씨 온도를 입력하세요 : ");
        scanf_s("%f", &c);
        f = (c * 9 / 5) + 32;
        printf("화씨 온도 : %.2f", f);
    }

    else if (tem == 'f') {
        printf("화씨 온도를 입력하세요 : ");
        scanf_s("%f", &f);
        c = (f - 32) * 5 / 9;
        printf("섭씨 온도 : %.2f", f);
    }

    else
        printf("잘못된 단위입니다.");

    return 0;
}

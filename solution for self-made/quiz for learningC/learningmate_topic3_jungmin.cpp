/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 3 - 한 명당 내야 할 금액 계산하기 (문정민)
  */

/*
한 명당 내야 할 금액 계산하기
입력 : 첫 번째 줄에 음식 종류가 주어진다.
두 번째 줄에 친구 수가 주어진다.
이후 n개의 줄에는 음식 가격과 수량이 공백을 사이에 두고 주어진다.
출력 : 지불해야 할 총 금액과 한 명당 지불해야 할 금액을 출력한다.
(단 한 명당 지불해야 할 금액은 소수점 2자리까지 나타낸다.)
*/

#include <stdio.h>

int main(void) 
{
    int sort = 0, friends = 0, price = 0, amount = 0, total = 0;
    
    printf("음식 종류 : ");
    scanf ("%d", &sort);
    
    printf ("\n친구 수 : ");
    scanf ("%d", &friends);
    
    for (int i = 0; i < sort; i++)
    {
        printf ("\n음식 가격과 수량 : ");
        scanf ("%d %d", &price, &amount);
        
        total = total + price * amount;
    }
    
    printf ("전체 금액 : %d\n", total);
    printf ("한 명당 게산해야 할 금액 : %.2f", (float)total / friends);
    
    return 0;
}

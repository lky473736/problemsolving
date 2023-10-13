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

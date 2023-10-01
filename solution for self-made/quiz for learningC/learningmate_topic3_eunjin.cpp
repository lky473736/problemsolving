/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 3 - 컴퓨터가 생성한 난수 맞추기 (한은진)
  */

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

int main(void) 
{
    srand (time(NULL));
    int random = rand() % 100; // 0부터 99까지 난수 생성
    int num;
    
    while (true) 
    {
        scanf ("%d", &num);
        
        if (num == random)
        {
            break;
        }
        
        else if (num > random)
        {
            printf ("입력한 숫자가 난수보다 큽니다.\n");
        }
        
        else
        {
            printf ("입력한 숫자가 난수보다 작습니다.\n");
        }
    }
    
    printf ("맞았습니다.");
    
    return 0;
}

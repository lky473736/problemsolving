/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 3 - 홀수, 짝수 판별기 (정예지)
  */

#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

int main(void) 
{
    int result = -1 ;
    int num;
    
    printf("3 이상의 정수를 입력하세요: ");
    scanf("%d", &num);
    
    if (num>=3)
    {
        switch (num % 2)
        {
            case 0 : // 짝수일 때
                result = 0;
            
            default : // 홀수일 때
                result = 1;
        }
    }
    
    else 
    {
        printf("다시 입력하세요.");
    }
    
    if (result == 0)
    {
        printf ("%d는 짝수입니다.", num);
    }
    else 
    {
        printf ("%d는 홀수입니다.", num);
    }
}

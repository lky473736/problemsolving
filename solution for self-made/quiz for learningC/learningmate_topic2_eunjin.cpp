/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 2 - 홀수 짝수 분류기 (한은진)
  */

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
   int a;

   printf("자연수를 입력하시오 : ");
   scanf("%d", &a); 

   for (int i = 1; i <= a; i++)
  {
     if (i % 2 == 0)
     {
       printf ("짝수\n");
     }
     else
     {
       printf ("홀수\n");
     }
  }
   return 0;
}

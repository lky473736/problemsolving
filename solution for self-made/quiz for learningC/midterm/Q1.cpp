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

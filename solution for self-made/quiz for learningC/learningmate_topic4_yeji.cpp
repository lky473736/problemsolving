/* 
  2023-2학기 가천대학교 학습공동체 : 팀 GPT (Gachon Programming Team)
  topic 4 - 2의 n승 별 출력기 (정예지)
  */


#include <stdio.h>

int main()
{
    int x, y;
    
    for (y = 1; y < 50; y = y * 2)
    {
        for (x = 0; x < y; x++)
        {
            printf ("*");
        }
        printf ("\n");
    }
    
    return 0;
}

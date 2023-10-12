#include <stdio.h>

int main()
{
    char star = '*';
    char blank = ' ';
    int n; // 층 수
    int counting = 0;
    
    scanf ("%d", &n); // 층 수 입력받음
    
    while (counting < n)
    {
        for (int i = 0; i < n - counting - 1; i++) // 공백
        {
            printf ("%c", blank);
        }
        
        for (int i = 0; i < 2 * (counting + 1) - 1; i++) // 별
        {
            printf ("%c", star);
        }
        
        printf ("\n"); // 개행
        
        counting++;
    }
}

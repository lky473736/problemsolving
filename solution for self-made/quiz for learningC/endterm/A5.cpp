#include <stdio.h>

int main()
{
    char string[10]; // 입력 받는 문자열
    char finding; // 찾아야 하는 문자
    int counting = 0; // 찾아야 하는 문자의 갯수
    
    gets(string);
    
    scanf ("%c", &finding);
    
    for (int i = 0; i < 10; i++)
    {
        if (finding == string[i])
        {
            counting += 1;
        }
    }
    
    printf ("%d", counting);
}

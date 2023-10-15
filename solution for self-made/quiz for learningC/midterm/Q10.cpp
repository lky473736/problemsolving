/*
    주의사항

    visual studio 19를 사용하시는 분들께선 아래 코드의 출력값이 이상하게 나올 수 있습니다. 
    원인은 본 코드는 gcc 컴파일러 기반으로 작성되었기 때문에 컴파일러 차이로 인하여 그런 것 같습니다.

    visual studio 19 사용자는 아래 주석으로 감싸진 코드를 참고해주세요.
*/

/*
    #include <stdio.h>

    int main()
    {
       char mode;
       int binary;

       scanf_s(" %c", &mode);
       scanf_s("%d", &binary);

       if (mode == 'O')
       {
          printf("%o", binary);
       }

       else if (mode == 'H')
       {
          printf("%x", binary);
       }
    }
*/

#include <stdio.h>

int main()
{
    char mode;
    int binary;
    
    scanf (" %c %d", &mode, &binary);
    
    if (mode == 'O')
    {
        printf ("%o", binary);
    }
    
    else if (mode == 'H')
    {
        printf ("%x", binary);
    }
}

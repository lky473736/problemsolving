
#include <stdio.h>

int main()
{
    int arr[5];
    int component;
    
    for (int i = 0; i < 5; i++)
    {
        scanf ("%d", &component);
        arr[i] = component;
    }
    
    int *point; // 포인터형 변수 startpoint 선언
    point = arr + 4; // 마지막 주소에 대응
    
    for (int i = 0; i < 5; i++)
    {
        printf ("arr[%d] == %d\n", 4 - i, *(point - i));
    }
}


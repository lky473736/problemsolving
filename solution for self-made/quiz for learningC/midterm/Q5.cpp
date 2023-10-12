#include <stdio.h>

int main()
{
    int x, y, z, min, max;
    
    scanf ("%d %d %d", &x, &y, &z);
    
    min = x; // 일단은 최솟값이 x라 가정
    max = x; // 일단은 최댓값이 x라 가정
    
    if (min > y)
    {
        min = y;
    }
    
    if (min > z)
    {
        min = z;
    }
    
    if (max < y)
    {
        max = y;
    }
    
    if (max < z)
    {
        max = z;
    }
    
    printf ("min : %d / max : %d", min, max);
}

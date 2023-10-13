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

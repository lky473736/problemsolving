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

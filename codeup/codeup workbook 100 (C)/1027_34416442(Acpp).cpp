#include <stdio.h>
#include <string.h>

int main()
{
    int y, d;
    int m;
    int zero1;
    int zero2;
    
    scanf ("%4d.%1d%1d.%1d%1d", &y, &zero1, &m, &zero2, &d);
    
    printf ("%d%d-%d%d-%d", zero2, d, zero1, m, y);
}

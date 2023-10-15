#include <stdio.h>
#include <string.h>

int main()
{
    int k;
    
    scanf ("%d", &k);
    
    printf ("[%d0000]\n", k / 10000);
    printf ("[%d000]\n", (k % 10000) / 1000);
    printf ("[%d00]\n", ((k % 10000) % 1000) / 100);
    printf ("[%d0]\n", (((k % 10000) % 1000) % 100) / 10);
    printf ("[%d]", (((k % 10000) % 1000) % 100) % 10);
}

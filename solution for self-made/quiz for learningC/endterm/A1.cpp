#include <stdio.h>

int main()
{
    int gugudan[9][9];
    
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            gugudan[i][j] = (i + 1) * (j + 1);
        }
    }
    
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            printf ("%d * %d == %d\n", i + 1, j + 1, gugudan[i][j]);
        }
        
        printf ("==============\n");
    }
}

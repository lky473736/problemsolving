/*
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
}*/

#include <stdio.h>

int main()
{
    int gugudan[9][9];
    
    /*
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            gugudan[i][j] = (i + 1) * (j + 1);
        }
    }*/
    
    int i, j;
    
    i = 0;
    while (i < 9)
    {
        j = 0;
        while (j < 9)
        {
            gugudan[i][j] = (i + 1) * (j + 1);
            j++;
        }
        i++;
    }
    
    i = 0;
    
    while (i < 9)
    {
        j = 0;
        
        while (j < 9)
        {
            printf ("%d * %d == %d\n", i + 1, j + 1, gugudan[i][j]);
            j++;
        }
        
        printf ("===========\n");
        i++;
    }
}

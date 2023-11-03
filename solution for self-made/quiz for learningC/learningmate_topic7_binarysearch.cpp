#include <stdio.h>
#include <stdbool.h>
#define ARRNUM 100

int middlepoint (int start, int end);

int main(void) 
{
    int arr[ARRNUM];
    
    for (int i = 0; i < ARRNUM; i++)
    {
        arr[i] = i + 1;
    }
    
    int findcompo = 0;
    int start = 1;
    int end = ARRNUM;
    
    int middlepointcompo = 50;
    
    int loopnum = 0;
    
    printf ("Input the num to find in 2 ~ 99 : ");
    scanf ("%d", &findcompo);
    
    while (true)
    {
        loopnum += 1;
        
        printf ("middle point : %d\n", middlepointcompo);
        
        if (middlepointcompo > findcompo)
        {  
            end = middlepointcompo;
        }
        
        else if (middlepointcompo < findcompo)
        {
            start = middlepointcompo;
        }
        
        else if (middlepointcompo == findcompo || start == findcompo || end == findcompo)
        {
            printf ("find the compo\n");
            printf ("loopnum : %d\n", loopnum);
            break;
        }
        
        middlepointcompo = middlepoint(start, end);
    }
}

int middlepoint (int start, int end)
{
    return (int)(end - start) / 2 + start;
}

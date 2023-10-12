/* <while문>
#include <stdio.h>

int main()
{
    int i = 0;
    int sum = 0;
    
    while (i <= 100)
    {
        sum += i;
        i++;
    }
    
    printf ("%d", sum);
}
*/

/* <for문>
#include <stdio.h>

int main()
{
    int sum = 0;
    
    for (int i = 1; i <= 100; i++)
    {
        sum += i;
    }
    
    printf ("%d", sum);
}
*/

/* <do-while문>
#include <stdio.h>

int main()
{
    int i = 1;
    int sum = 0;
    
    do
    {
        sum += i;
        i++;
    }
    while (i <= 100);
    
    printf ("%d", sum);
}
*/

/* <goto문>
#include <stdio.h>

int main()
{
    int i = 0;
    int sum = 0;

k : 
    sum += i;

    if (i < 100) 
    {
        i++;
        goto k;
    }
    
    printf ("%d", sum);
}
*/

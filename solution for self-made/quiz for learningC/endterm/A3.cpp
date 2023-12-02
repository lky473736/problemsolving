#include <stdio.h>

int fact(int n);

int main()
{
    auto int n;
    
    scanf ("%d", &n);

    printf ("factorial n : %d", fact(n));
}

int fact(int n)
{
    if (n == 1)
    {
        return 1;
    }
    
    else
    {
        return n * fact(n - 1); // recursion
    }
}
		



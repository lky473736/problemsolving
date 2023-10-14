#include <stdio.h>

int main() {
    long y, m, d;
    
    scanf("%ld.%ld.%ld", &y, &m, &d);
    
    printf("%04ld.%02ld.%02ld", y, m, d);

    return 0;
}

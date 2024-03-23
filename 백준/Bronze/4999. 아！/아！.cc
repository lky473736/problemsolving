#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    char jaehwan[1001];
    char doctor[1001];
    
    scanf ("%s", jaehwan);
    scanf ("%s", doctor);
    
    if (strlen(jaehwan) < strlen(doctor)) {
        printf ("no\n");
    }
    
    else {
        printf ("go\n");
    }
    
    return 0;
}
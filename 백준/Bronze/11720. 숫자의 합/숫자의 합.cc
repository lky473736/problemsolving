#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    int N;
    scanf ("%d", &N);
    
    int suma = 0;
    
    std::string s;
    std::cin >> s;
    
    for (int i = 0; i < s.size(); i++) {
        suma += int(s[i]) - 48;
    }
    
    printf ("%d\n", suma);
    
    return 0;
}
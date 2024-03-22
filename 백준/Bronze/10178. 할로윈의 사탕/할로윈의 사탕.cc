#include <cstdio>
#include <iostream>

int main() {
    int N;
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++) {
        int c, v;
        scanf ("%d %d", &c, &v);
        
        std::cout << "You get " << int(c/v) << " piece(s) and your dad gets " << c%v << " piece(s)." << std::endl;
    }
    
    return 0;
}
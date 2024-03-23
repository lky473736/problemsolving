#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    // 임의 정밀도 / 큰 숫자 연산 필요
    // int N;
    // scanf ("%d", &N);
    
    // for (int i = 0; i < N; i++) {
    //     int K;
    //     scanf ("%d", &K);
        
    //     if (K % 2 == 0) {
    //         printf ("even\n");
    //     }
        
    //     else {
    //         printf ("odd\n");
    //     }
    // }
    
    int N;
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++) {
        std::string s;
        std::cin >> s;
        
        if ((int(s[s.size() - 1])-48) % 2 == 0) {
            printf ("even\n");
        }
        
        else {
            printf ("odd\n");
        }
    }
    
    return 0;
}
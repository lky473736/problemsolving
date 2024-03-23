#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <vector>

int main() {
    int A, B, C, D;
    std::cin >> A >> B;
    std::cin >> C >> D;
    
    // 분자는 모두 동일하니, 각각의 분모가 최소가 되는 애 찾기
    // double cir0, cir1, cir2, cir3;
    // cir0 = double((A*D + B*C) / C*D);
    // cir1 = double((A*D + B*C) / B*D);
    // cir2 = double((A*D + B*C) / A*B);
    // cir3 = double((A*D + B*C) / A*C);
    // double arr[] = {cir0, cir1, cir2, cir3};
    
    // double max = std::max({cir0, cir1, cir2, cir3})
    // printf ("%lf %lf %lf %lf\n", cir0, cir1, cir2, cir3);
    
    int arr[4];
    arr[0] = C*D;
    arr[1] = B*D;
    arr[2] = A*B;
    arr[3] = A*C;
    
    int min = arr[0];
    
    // findMin 완전탐색 알고리즘
    for (int i = 0; i < 4; i++) {
        if (min > arr[i]) {
            min = arr[i];
        }
    }
    
    for (int i = 0; i < 4; i++) {
        if (min == arr[i]) {
            printf ("%d\n", i);
            break;
        }
    }
	
	return 0;
}
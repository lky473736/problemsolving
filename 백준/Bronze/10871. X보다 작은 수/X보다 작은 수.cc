#include <iostream>

int main() {
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int N, X;
    int compo;
    std::cin >> N >> X;
    
    for (int i = 0; i < N; i++) {
        std::cin >> compo;
        
        if (compo < X) {
            std::cout << compo << " ";
        }
    }
    
    return 0;
}
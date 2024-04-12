#include <iostream>
#include <cstdio>
#include <queue>

int main() {
    std::queue<int> queue;
    int N;
    int counting = 0;
    
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++) {
        std::string command;
        std::cin >> command;
        int _ = getchar();
        
        if (command.compare("push") == 0) {
            int X;
            scanf ("%d", &X);
            int _ = getchar();
            
            queue.push(X);
            counting += 1;
        }
        
        if (command.compare("pop") == 0) {
            if (counting > 0) {
                std::cout << queue.front() << "\n";
                queue.pop();
                counting -= 1;
            }
            
            else {
                std::cout << -1 << "\n";
            }
        }
        
        if (command.compare("size") == 0) {
            std::cout << counting << "\n";
        }
        
        if (command.compare("empty") == 0) {
            if (counting == 0) {
                std::cout << 1 << "\n";
            }
            
            else {
                std::cout << 0 << "\n";
            }
        }
        
        if (command.compare("front") == 0) {
            if (counting == 0) {
                std::cout << -1 << "\n";
            }
            
            else {
                std::cout << queue.front() << "\n";
            }
        }
        
        if (command.compare("back") == 0) {
            if (counting == 0) {
                std::cout << -1 << "\n";
            }
            
            else {
                std::cout << queue.back() << "\n";
            }
        }
    }
    
    return 0;
}
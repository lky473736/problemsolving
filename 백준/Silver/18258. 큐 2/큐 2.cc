#include <iostream>
#include <cstdio>
#include <queue>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    std::queue<int> queue;
    long long int N;
    long long int counting = 0;
    
    std::cin >> N;
    
    for (int i = 0; i < N; i++) {
        std::string command;
        std::cin >> command;

        if (command.compare("push") == 0) {
            long long int X;
            std::cin >> X;
            
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
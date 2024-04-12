#include <iostream>
#include <cstdio>
#include <deque>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    std::deque<int> deque;
    long long int N;
    long long int counting = 0;
    
    std::cin >> N;
    
    for (int i = 0; i < N; i++) {
        std::string command;
        std::cin >> command;

        if (command.compare("push_front") == 0) {
            long long int X;
            std::cin >> X;
            
            deque.push_front(X);
            counting += 1;
        }
        
        if (command.compare("push_back") == 0) {
            long long int X;
            std::cin >> X;
            
            deque.push_back(X);
            counting += 1;
        }
        
        if (command.compare("pop_front") == 0) {
            if (counting == 0) {
                std::cout << -1 << "\n";
            }
            
            else {
                std::cout << deque.front() << "\n";
                deque.pop_front();
                counting -= 1;
            }
        }
        
        if (command.compare("pop_back") == 0) {
            if (counting == 0) {
                std::cout << -1 << "\n";
            }
            
            else {
                std::cout << deque.back() << "\n";
                deque.pop_back();
                counting -= 1;
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
                std::cout << deque.front() << "\n";
            }
        }
        
        if (command.compare("back") == 0) {
            if (counting == 0) {
                std::cout << -1 << "\n";
            }
            
            else {
                std::cout << deque.back() << "\n";
            }
        }
    }
    
    return 0;
}
#include <iostream>
#include <cstdio>
#include <deque>

int main() {
    std::cin.tie(0);
    std::cin.sync_with_stdio(0);
    
    std::deque<int> dq;
    
    int counting = 0;
    int N = 0;
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++) {
        int operation = 0, X = 0;
        scanf ("%d", &operation);
        
        switch (operation) {
            case 1 :
                scanf ("%d", &X);
                dq.push_front (X);
                counting += 1;
                break;
                
            case 2 : 
                scanf ("%d", &X);
                dq.push_back (X);
                counting += 1;
                break;
                
            case 3 : 
                if (counting != 0) {
                    std::cout << dq.front() << "\n";
                    dq.pop_front();
                    counting -= 1;
                }
                else {
                    std::cout << -1 << "\n";
                }
                break;
                
            case 4 :
                if (counting != 0) {
                    std::cout << dq.back() << "\n";
                    dq.pop_back();
                    counting -= 1;
                }
                else {
                    std::cout << -1 << "\n";
                } 
                break;
                
            case 5 : 
                std::cout << counting << "\n";
                break;
                
            case 6 : 
                if (counting == 0) {
                    std::cout << 1 << "\n";
                }
                else {
                    std::cout << 0 << "\n";
                }
                break;
                
            case 7 : 
                if (counting != 0) {
                    std::cout << dq.front() << "\n";
                }
                else {
                    std::cout << -1 << "\n";
                } 
                break;
                
            case 8 :
                if (counting != 0) {
                    std::cout << dq.back() << "\n";
                }
                else {
                    std::cout << -1 << "\n";
                } 
                break;
                
            default : 
                break;
        }
    }
    
    return 0;
}
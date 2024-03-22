#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int determine(int a, std::string oper, int b);

int main() {
    int i = 0;
    
    std::map<std::string, int> operators = {
        {">", 1},
        {">=", 2},
        {"<", 3},
        {"<=", 4},
        {"==", 5},
        {"!=", 6}
    };
    
    while (true) {
        std::string oper;
        int operand1;
        int operand2;
        
        std::cin >> operand1 >> oper >> operand2;
        
        if (oper == "E") {
            break;
        }
        
        std::string rst;
        
        if (determine(operand1, oper, operand2) == 1) {
            rst = "true";
        } 
        
        else {
            rst = "false";
        }
        
        printf("Case %d: %s\n", ++i, rst.c_str());
    }
    
    return 0;
}

int determine(int a, std::string oper, int b) {
    std::map<std::string, int> operators = {
        {">", 1},
        {">=", 2},
        {"<", 3},
        {"<=", 4},
        {"==", 5},
        {"!=", 6}
    };

    switch (operators[oper]) {
        case 1:
            if (a > b) {
                return 1;
            }
            return 0;
            
        case 2:
            if (a >= b) {
                return 1;
            }
            return 0;
            
        case 3:
            if (a < b) {
                return 1;
            }
            return 0;
            
        case 4:
            if (a <= b) {
                return 1;
            }
            return 0;
            
        case 5:
            if (a == b) {
                return 1;
            }
            return 0;
            
        case 6:
            if (a != b) {
                return 1;
            }
            return 0;
            
        default:
            return 0;
    }
}

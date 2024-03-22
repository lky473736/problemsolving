#include <cstdio>
#include <iostream>
#include <map>
#include <string>

int main() {
    std::map<std::string, std::string> credit;
    credit["A+"] = "4.3";
    credit["A0"] = "4.0";
    credit["A-"] = "3.7";
    credit["B+"] = "3.3";
    credit["B0"] = "3.0";
    credit["B-"] = "2.7";
    credit["C+"] = "2.3";
    credit["C0"] = "2.0";
    credit["C-"] = "1.7";
    credit["D+"] = "1.3";
    credit["D0"] = "1.0";
    credit["D-"] = "0.7";
    credit["F"] = "0.0";
    
    std::string score;
    std::cin >> score;
    
    std::cout << credit.at(score) << std::endl;
    
    return 0;
}
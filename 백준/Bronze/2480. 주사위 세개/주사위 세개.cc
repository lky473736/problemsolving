#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int dice[3] = {}, rst;
    cin >> dice[0] >> dice[1] >> dice[2];
    
    if (dice[0] == dice[1] && dice[0] == dice[2]) {
        rst = 10000 + dice[0] * 1000;
    }
    
    else {
        if (dice[0] == dice[1] || dice[0] == dice[2]) {
            rst = 1000 + dice[0] * 100;
        }
        
        else if (dice[1] == dice[2]) {
            rst = 1000 + dice[1] * 100;
        }
        
        else {
            rst = max({*dice, *(dice+1), *(dice+2)}) * 100;
        }
    }
    
    cout << rst;
    
    return 0;
}
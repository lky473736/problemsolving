#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int max, compo, idx;
    for (int i = 0; i < 9; i++) {
        cin >> compo;
        
        if (i == 0) {
            max = compo;
            idx = i;
        }
        
        else {
            if (max < compo) {
                max = compo;
                idx = i;
            }
        }
    }
    
    cout << max << '\n' << idx+1;
    
    return 0;
}
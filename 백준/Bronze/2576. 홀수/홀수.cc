#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int sum = 0, compo = 0, min = 0, cnt = 0;
    
    for (int i = 0; i < 7; i++) {
        cin >> compo;
        
        if (compo % 2 != 0) {
            sum += compo;
            cnt++;
            
            if (cnt == 1) {
                min = compo;
            }
            
            else {
                if (min > compo) {
                    min = compo;
                }
            }
        }
    }
    
    if (cnt != 0) {
        cout << sum << '\n' << min;
    }
    
    else {
        cout << -1;
    }
    
    return 0;
}
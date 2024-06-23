#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int arr[4], cnt = 0;
    
    for (int i = 0; i < 3; i++) {
        cin >> arr[0] >> arr[1] >> arr[2] >> arr[3];
        
        cnt = 0;
        
        for (int j = 0; j < 4; j++) {
            if (arr[j] == 1) {
                cnt++;
            }
        }
        
        switch (cnt) {
            case 0 : cout << "D\n"; break;
            case 1 : cout << "C\n"; break;
            case 2 : cout << "B\n"; break;
            case 3 : cout << "A\n"; break;
            case 4 : cout << "E\n"; break;
            
            default : 
                break;
        }
    }
    
    return 0;
}
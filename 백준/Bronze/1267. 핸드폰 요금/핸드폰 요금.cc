#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int Y = 0, M = 0;
    int N = 0, sec = 0;
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> sec;
        
        // Y
        Y += 10 * ((sec / 30) + 1);
        
        // M
        M += 15 * ((sec / 60) + 1);
    }
    
    if (Y < M) {
        cout << "Y " << Y;
    }
    
    else if (Y > M) {
        cout << "M " << M;
    }
    
    else {
        cout << "Y M " << Y;
    }
    
    return 0;
}
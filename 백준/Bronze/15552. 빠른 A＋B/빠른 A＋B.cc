#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    long long T = 0;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int A, B;
        cin >> A >> B;
        cout << A + B << '\n';
    }
    
    return 0;
}
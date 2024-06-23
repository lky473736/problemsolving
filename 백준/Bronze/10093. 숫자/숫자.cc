#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    long long A, B;
    cin >> A >> B;
    
    
    if (A < B) {
        cout << abs(A - B) - 1 << '\n';
        for (long long i = A+1; i <= B-1; i++) {
            cout << i << ' ';
        }
    }
    
    else if (A > B) {
        cout << abs(A - B) - 1 << '\n';
        for (long long i = B+1; i <= A-1; i++) {
            cout << i << ' ';
        }
    }
    
    else {
        cout << 0;
    }
    
    return 0;
}
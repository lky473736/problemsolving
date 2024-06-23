#include <iostream>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int A, B;
    cin >> A >> B;
    
    cout << A + B << '\n';
    cout << A - B << '\n';
    cout << A * B << '\n';
    cout << A / B << '\n';
    cout << A % B << '\n';
    
    return 0;
}

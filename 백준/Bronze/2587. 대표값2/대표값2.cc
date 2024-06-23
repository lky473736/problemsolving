#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int arr[5], sum = 0;
    
    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
        sum += arr[i];
    }    
    
    sort(arr, arr+5);
    
    cout << sum/5 << '\n' << arr[2];
    
    return 0;
}
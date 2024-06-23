#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    long long arr[3];
    cin >> arr[0] >> arr[1] >> arr[2];
    
    sort(arr, arr+3);
    
    cout << *arr << ' ' << *(arr+1) << ' ' << *(arr+2);
    
    return 0;
}
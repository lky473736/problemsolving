#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n;
    cin >> n;
    
    long long arr[5001];
    
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    sort(arr, arr+n);
    
    long long min = 4000000000;
    long long t1 = 0, t2 = 0, t3 = 0;
    
    for (int i = 0; i < (sizeof(arr)/sizeof(*arr))-2; i++) {
        long long left = i+1;
        long long right = n-1;
        
        while (left < right) {
            long long rst = arr[i] + arr[left] + arr[right];
            
            if (abs(rst) <= abs(min)) {
                t1 = arr[i];
                t2 = arr[left]; 
                t3 = arr[right];
                
                min = rst;
            }
            
            if (rst > 0) {
                right -= 1;
            }
            
            else if (rst < 0) {
                left += 1;
            }
            
            else {
                cout << t1 << ' ' << t2 << ' ' << t3;
                return 0;
            }
        }
    }
    
    cout << t1 << ' ' << t2 << ' ' << t3;  
    return 0;
}
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    
    int arr[20];
    for (int i = 0; i < 20; i++) {
        arr[i] = i+1;
    }
    
    int a, b, term;
    for (int i = 0; i < 10; i++) {
        cin >> a >> b;
        
        if (a == b) {
            ;
        }
        
        else {
            term = b - a + 1;
            
            for (int j = 0; j < term/2; j++) {
                int temp = arr[a+j-1];
                arr[a+j-1] = arr[b-j-1];
                arr[b-j-1] = temp;
            }
            
            // int *section = new int[term];
            // int cnt = 0;
            // for (int j = a-1; j <= b-1; j++) {
            //     section[cnt++] = arr[j];
            // }
            
            // sort(section, section+term, greater<int>());

            // for (int j = 0; j < term; j++) {
            //     arr[a-1+j] = section[j];
            // }
        }
    }
    
    for (int i = 0; i < 20; i++) {
        cout << arr[i] << ' ';
    }
    
    return 0;
}
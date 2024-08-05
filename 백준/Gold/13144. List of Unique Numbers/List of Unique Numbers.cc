// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int N;
//     cin >> N;
    
//     vector<int> arr;
//     for (int i = 0; i < N; i++) {
//         cin >> arr[i];
//     }
    
//     int cnt = 0;
    
//     for (int i = 0; i < n; i++) {
//         vector<int> temp;
//         for (int j = i; j < n; j++) {
            
//         }
//     }
    
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std; 

int main() {
    int N = 0;
    long long rst = 0;
    
	cin >> N;
	vector<int> arr(N);
	
	for (int i = 0; i < N; i++) {
	    cin >> arr[i];
	}
	
	vector<bool> visited(*max_element(arr.begin(), arr.end()) + 1, false); 
	
	int start = 0, end = 0;
	
// 	for (int start = 0; start < N; start++) {
// 	    int cnt = 0;
	    
// 		while (end < N) {
// 			if (visited[arr[end]] == true) {
// 			    break; 
// 			}
			
// 			visited[arr[end++]] = true;
// 			cnt++;
// 		}
		
// 		rst += cnt;
// 		visited[arr[start]] = false; 
// 	}
	
// 	cout << rst << '\n';

    // int cnt = 0;
    
    while (start < N) {
        while (end < N) {
            if (visited[arr[end]] == true) {
                break; 
            }
            
            visited[arr[end]] = true;
            end++;
            // cnt++;
        }
        
        rst += end-start;
        
        visited[arr[start]] = false;
        start++;
    }
    
    cout << rst << '\n';
    
    return 0;
}
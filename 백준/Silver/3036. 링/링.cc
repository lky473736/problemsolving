#include <bits/stdc++.h>
using namespace std;

int euclidean (int a, int b) {
	int r;
	
	while (b != 0) {
		r = a % b;
		a = b;
		b = r;
	}
	
	return a;
}

int main() {
    int N;
    cin >> N;
    
    int arr[100];
    for (int i = 0; i < N; i++) {
        int compo;
        cin >> compo;
        
        arr[i] = compo;
    }
    
    for (int i = 1; i < N; i++) {
        int gcd = euclidean(arr[0], arr[i]);
        cout << arr[0] / gcd << '/' << arr[i] / gcd << '\n';
    }
    
    return 0;
}
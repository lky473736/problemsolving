#include <bits/stdc++.h>
using namespace std;
// typedef long long ll;

int main(void) {
    ios::sync_with_stdio(false); cin.tie(0);
    
    int arr[20];
    for (int i = 0; i < 20; i++) arr[i] = i+1;
    
    for (int i = 0; i < 10; i++) {
        int x, y; cin >> x >> y;
        vector<int> temp(20);

        for (int j = 0; j < y-x+1; j++)     temp[x-1+j] = arr[y-1-j];
        // for (int j = 0; j < y-x+1; j++)   cout << temp[j] << '\n';
        for (int j = x-1; j < y; j++)     arr[j] = temp[j];
    }

    for (int i = 0; i < 20; i++) cout << arr[i] << ' ';
    return 0;
}
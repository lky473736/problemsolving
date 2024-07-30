#include <iostream>
using namespace std;

int main() {
    int cnt = 1;
    
    while (true) {
        int L, P, V;
        cin >> L >> P >> V;

        if (L == 0 && P == 0 && V == 0) {
            break;
        }
        
        int i = V / P;
        int j = V % P;
        if (L < j) {
            j = L;
        }

        int rst = L * i + j;

        cout << "Case "<< cnt << ": " << rst << '\n';
        cnt++;
    }
    
    return 0;
}
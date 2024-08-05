#include <bits/stdc++.h>
using namespace std;

/*
import sys 

n = int(sys.stdin.readline())

rst = 0
Alist = list()
Blist = list()
Clist = list()
Dlist = list() 

for i in range (n) :
    a, b, c, d = map(int, sys.stdin.readline().split())
    
    Alist.append (a)
    Blist.append (b)
    Clist.append (c)
    Dlist.append (d)

aplusb = dict()
# keys = set()

for compo_a in Alist : 
    for compo_b in Blist :
        plus1 = compo_a + compo_b
        
        if plus1 not in aplusb : 
            aplusb[plus1] = 1 
            # keys.add(plus1)
            
        else :
            aplusb[plus1] += 1

for compo_c in Clist :
    for compo_d in Dlist :
        plus2 = -(compo_c + compo_d)
        
        if plus2 in aplusb :
            rst += aplusb[plus2]
            # rst += 1

print (rst)
*/

int main() {    
    int n;  
    cin >> n;
    
    vector<long long> A(n);
    vector<long long> B(n);
    vector<long long> C(n);
    vector<long long> D(n);
    
    for (int i = 0; i < n; i++) {
        cin >> A[i] >> B[i] >> C[i] >> D[i];
    }
    
    unordered_map<long long, int> aplusb;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            long long plus1 = A[i] + B[j];
            
            if (aplusb.find(plus1) != aplusb.end()) {
                aplusb[plus1] += 1;
            }
            
            else {
                aplusb.insert({plus1, 1});
            }
        }
    }
    
    int rst = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            long long plus2 = -1 * C[i] -1 * D[j];
            
            if (aplusb.find(plus2) != aplusb.end()) {
                rst += aplusb[plus2];
            }
        }
    }
    
    cout << rst;
    
    return 0;
}


// #include <bits/stdc++.h>
// using namespace std;

// int main() {
//     int n;
//     cin >> n;
    
//     vector<long long> A(n);
//     vector<long long> B(n);
//     vector<long long> C(n);
//     vector<long long> D(n);
    
//     for (int i = 0; i < n; i++) {
//         cin >> A[i] >> B[i] >> C[i] >> D[i];
//     }
    
//     unordered_map<long long, int> aplusb;
    
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             long long plus1 = A[i] + B[j];
//             aplusb[plus1]++;
//         }
//     }
    
//     int rst = 0;
    
//     for (int i = 0; i < n; i++) {
//         for (int j = 0; j < n; j++) {
//             long long plus2 = -C[i] - D[j];
//             if (aplusb.find(plus2) != aplusb.end()) {
//                 rst += aplusb[plus2];
//             }
//         }
//     }
    
//     cout << rst << endl;
    
//     return 0;
// }

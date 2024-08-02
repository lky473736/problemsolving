import sys

n = int(sys.stdin.readline())
# nset = set()
nlist = list()

for i in range (n) :
    compo = int(sys.stdin.readline())
    nlist.append (compo)
    
    # if compo not in nset : 
    #     nlist.append (compo)
    #     nset.add(compo)

nlist.sort()

rst = 0

'''
#include <bits/stdc++.h>
using namespace std;

double a[100000];
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)2
        cin >> a[i];
    sort(a, a + n);
    int maxi = 0;
    for (int i = 0; i < n - 2; i++)
        maxi = max(maxi, (int)abs(a[i] - 2 * a[i + 1] + a[n - 1]));
    for (int i = n - 1; i > 1; i—)
        maxi = max(maxi, (int)abs(a[0] - 2 * a[i - 1] + a[i]));
    cout << maxi;
}
'''

for i in range (0, n-2) :
    if rst < abs(nlist[n-1] + nlist[i] - nlist[i+1]*2) :
        rst = abs(nlist[n-1] + nlist[i] - nlist[i+1]*2)

for i in range (n-1, 1, -1) :
    if rst < abs(nlist[0] -2 * nlist[i-1] + nlist[i]) :
        rst = abs(nlist[0] -2 * nlist[i-1] + nlist[i])

print (rst)
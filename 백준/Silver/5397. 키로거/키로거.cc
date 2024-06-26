#include <bits/stdc++.h>
using namespace std;

const long long mx = 1000005;
long long pre[mx];
long long nxt[mx];
char datas[mx];

void insert(long long &cursor, long long &unused, char dta) {
    datas[unused] = dta;
    nxt[unused] = nxt[cursor];
    pre[unused] = cursor;
    
    if (nxt[cursor] != -1) {
        pre[nxt[cursor]] = unused;
    }
    
    nxt[cursor] = unused;
    
    cursor = unused; 
    unused++;
}

void erase(long long &cursor) {
    if (cursor == 0) return; 
    long long to_erase = cursor;
    cursor = pre[cursor];
    nxt[cursor] = nxt[to_erase];
    
    if (nxt[to_erase] != -1) {
        pre[nxt[to_erase]] = cursor;
    }
}

void traverse() {
    long long cur = nxt[0];
    
    while (cur != -1) {
        cout << datas[cur];
        cur = nxt[cur];
    }
    
    cout << '\n';
}

int main() { 
    cin.tie(0);
    ios::sync_with_stdio(0);
    
    int N;
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        long long cursor = 0;
        long long unused = 1;
        
        fill(pre, pre+mx, -1);
        fill(nxt, nxt+mx, -1);
        
        string sentence;
        cin >> sentence;
        
        for (char c : sentence) {
            if (c == '<') {
                if (cursor != 0) {
                    cursor = pre[cursor];
                }
            } 
            
            else if (c == '>') {
                if (nxt[cursor] != -1) {
                    cursor = nxt[cursor];
                }
            } 
            
            else if (c == '-') {
                if (cursor != 0) {
                    erase(cursor);
                }
            } 
            
            else {
                insert(cursor, unused, c);
            }
        }
        
        traverse();
    }
    
    return 0;
}

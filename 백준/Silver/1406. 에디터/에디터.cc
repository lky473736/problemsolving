#include <bits/stdc++.h>
using namespace std;

const long long mx = 1000005;
long long unused = 1;
long long cursor = 0;

char datas[mx];
long long pre[mx];
long long nxt[mx];

void insert(long long addr, char dta) {
    datas[unused] = dta;
    nxt[unused] = nxt[addr];
    pre[unused] = addr;
    
    if (nxt[addr] != -1) {
        pre[nxt[addr]] = unused;
    }
    
    nxt[addr] = unused;
    
    unused++;
}

void erase(long long addr) {
    nxt[pre[addr]] = nxt[addr];
    if (nxt[addr] != -1) {
        pre[nxt[addr]] = pre[addr];
    }
}

void traverse() {
    long long cur = nxt[0];
    
    while (cur != -1){
        cout << datas[cur];
        cur = nxt[cur];
    }
}

int main() { 
    cin.tie(0);
    ios::sync_with_stdio(0);

    // Initialize the linked list
    fill(pre, pre + mx, -1);
    fill(nxt, nxt + mx, -1);
    
    string default_data;
    cin >> default_data;
    
    for (auto c : default_data) {
        insert(cursor, c);
        cursor++;
    }
    
    int N;
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        char command;
        cin >> command;
        
        switch (command) {
            case 'P': {
                char input_data;
                cin >> input_data;
                insert(cursor, input_data);
                cursor = nxt[cursor];
                break;
            }
            case 'B': {
                if (cursor != 0) {
                    erase(cursor);
                    cursor = pre[cursor];
                }
                break;
            }
            case 'L': {
                if (pre[cursor] != -1) {
                    cursor = pre[cursor];
                }
                break;
            }
            case 'D': {
                if (nxt[cursor] != -1) {
                    cursor = nxt[cursor];
                }
                break;
            }
            default:
                break;
        }
    }
    
    traverse();
    
    return 0;
}
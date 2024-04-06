#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>

int main() {
    int N, K;
    scanf ("%d %d", &N, &K);
    
    std::queue<int> q;
    std::vector<int> v;
    
    for (int i = 1; i <= N; i++) {
        q.push (i);
    }
    
    while (N > 0) {
        int ind = 0;
        
        for (int i = 0; i < K; i++) {
            if (ind == K) {
                ind = 0;
            }
            
            ind += 1;
        }
        
        for (int i = 0; i < ind-1; i++) {
            int t = q.front();
            q.pop();
            q.push(t);
        }
        
        int l = q.front();
        q.pop();
        v.push_back(l);
        
        N -= 1;
    }
    
    std::cout << "<";
    for (int i = 0; i < v.size(); i++) {
        if (i == v.size()-1) {
            std::cout << v[i];
            break;
        }
        std::cout << v[i] << ", ";
    }
    std::cout << ">" << std::endl;
    
    return 0;
}

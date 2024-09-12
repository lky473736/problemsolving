#include <bits/stdc++.h>
using namespace std;

// n번째 소수를 구하는 함수
vector<int> getPrimes(int n) {
    int limit = n * log(n) + n * log(log(n)); // 소수 추정을 위한 상한선
    vector<bool> isPrime(limit + 1, true);
    vector<int> primes;
    
    isPrime[0] = isPrime[1] = false; // 0과 1은 소수가 아님
    
    for (int i = 2; i <= limit && primes.size() < n; ++i) {
        if (isPrime[i]) {
            primes.push_back(i);
            for (int j = i * 2; j <= limit; j += i) {
                isPrime[j] = false;
            }
        }
    }
    return primes;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int n, k;
    cin >> n >> k;
    
    if (n == 1) {
        switch(k) {
            case 1 : 
                cout << 0 << ' ' << 1;
                return 0;
                
            case 2 : 
                cout << 1 << ' ' << 1;
                return 0;
        }
    }
    
    else if (n == 2) {
        switch(k) {
            case 1 : 
                cout << 0 << ' ' << 1;
                return 0;
                
            case 2 : 
                cout << 1 << ' ' << 2;
                return 0;
                
            case 3 : 
                cout << 1 << ' ' << 1;
                return 0;
        }
    }
    
    else {
        vector<int> primes = getPrimes(5000);
        int rest_num = 3;
        vector<pair<int, int>> v1;
        v1.push_back({0, 0})
        
        while (rest_num >= n) {
            int num = 1;
            while (num // )
                v1.push_back({num,  })
        }
    }
    
    
    
    return 0;
}

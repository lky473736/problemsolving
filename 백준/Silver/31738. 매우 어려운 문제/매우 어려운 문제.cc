#include <iostream>
#include <cstdio>

typedef long long ll;

ll factorial (ll n, ll m);
    
int main()
{
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
	
    long long int N;
    long long int M;
    scanf ("%lld %lld", &N, &M);
    
    std::cout << factorial(N, M) << '\n';

    return 0;
}

// int factorial(long long int n, int m) {
//     int result = 1;
    
//     for (int i = 1; i <= n; i++) {
//         // result = (result * i) % m;  // 중간 결과를 m으로 나눈 나머지를 계산
//         result *= i;
//         result %= m;
//     }
    
//     return result;
// }

ll factorial (ll n, ll m) {
    ll result = 1;
    
    for (ll i = 1; i <= n; i++) {
        result = (result * i) % m;
        
        if (result == 0) {
            return 0;
        }
    }
    
    return result;
}
#include <iostream>
#include <algorithm>

int main() 
{
    long long X, K;
    long long ans;
    long long j;
    
	std::cin >> X >> K;

	long long Y = 0;
    int kidx = 0;
    
    for (int i = 0; i < 65; i++)
    {
        if((X >> i) & 1LL) 
        {
            continue; 
        }
        
        if ((K >> kidx) & 1LL)
        {
            Y |= (1LL << i);
        }
        
        kidx++;
    }

	std::cout << Y;
	
	return 0;
}


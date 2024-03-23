#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    int N = 0;
	int W = 0;
	int H = 0;
	int length = 0;

	std::cin >> N >> W >> H;

	int M = W * W + H * H;

	for (int i = 0; i < N; i++)
	{
		std::cin >> length;
		
		if (pow(length, 2) <= M) {
			std::cout << "DA" << std::endl;
		}
		
		else {
			std::cout << "NE" << std::endl;
		}
	}
	
	return 0;
}
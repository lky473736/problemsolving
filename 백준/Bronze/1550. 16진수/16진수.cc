#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    int x;
    
    std::map<char, int> hexa;
    
    hexa['0'] = 0;
    hexa['1'] = 1;
    hexa['2'] = 2;
    hexa['3'] = 3;
    hexa['4'] = 4;
    hexa['5'] = 5;
    hexa['6'] = 6;
    hexa['7'] = 7;
    hexa['8'] = 8;
    hexa['9'] = 9;
    hexa['A'] = 10;
    hexa['B'] = 11;
    hexa['C'] = 12;
    hexa['D'] = 13;
    hexa['E'] = 14;
    hexa['F'] = 15;
    
    std::string s;
    
    int digit = 0;
    int suma = 0;
    
    std::cin >> s;
    
    for (int i = s.size()-1; i >= 0; i--) {
        suma += hexa[s[i]] * pow(16, digit);
        digit += 1;
    }
    
    printf ("%d\n", suma);
	
	return 0;
}
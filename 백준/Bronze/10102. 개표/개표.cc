/* #include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>
#include <cmath>

int main() {
    int A, B;
    int V;
    
    std::string s;
    std::cin >> V >> s;
    
    for (int i = 0; i < V; i++) {
        if (s[i] == 'A') {
            A += 1;
        }
        
        else if (s[i] == 'B') {
            B += 1;
        }
    }

    if (A > B) {
        printf ("A\n");
    }
    
    else if (A < B) {
        printf ("B\n");
    }
    
    else {
        printf ("Tie\n");
    }
	
	return 0;
} */

#include <iostream>
#include <string>

int main() {
    int v,a=0,b=0;
    std::string k;
    std::cin >> v >> k;
    for (int i = 0; i < v; i++)
    {
        if (k[i] == 'A')
            a++;
        else
            b++;
    }
    if (a == b) { std::cout << "Tie" << '\n';}
    else
        printf("%c\n", a < b ? 'B' : 'A');
}
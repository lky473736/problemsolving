#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    std::map<int, int> alphabet;
    
    for (int i = 0; i < 26; i++) {
        int apb = 65+i;
        alphabet[apb] = i+1;
    }
    
    int T = 0;
    scanf ("%d", &T);
    
    for (int i = 0; i < T; i++) {
        char s1[21], s2[21];
        scanf ("%s %s", s1, s2);
        
        printf ("Distances: ");
        
        for (int j = 0; j < strlen(s1); j++) {
            int oper1 = alphabet.at((int)s1[j]);
            int oper2 = alphabet.at((int)s2[j]);
            
            if (oper1 <= oper2) {
                printf ("%d ", oper2-oper1);
            }
            
            else if (oper1 > oper2) {
                printf ("%d ", (oper2+26) - oper1);
            }
        }
        
        printf ("\n");
    }
    
    return 0;
}
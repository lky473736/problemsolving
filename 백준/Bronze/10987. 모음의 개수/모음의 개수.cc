#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    int num_vowel = 0;
    char vowels[5] = {'a', 'e', 'i', 'o', 'u'};
    char S[101];
    
    scanf ("%s", S);
    
    for (int i = 0; i < strlen(S); i++) {
        for (int j = 0; j < 5; j++) {
            if (S[i] == vowels[j]) {
                num_vowel += 1;
            }
        }
    }
    
    printf ("%d\n", num_vowel);
    
    return 0;
}
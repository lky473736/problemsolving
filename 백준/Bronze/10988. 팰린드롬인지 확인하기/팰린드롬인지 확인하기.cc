#include <cstdio>
#include <iostream>
#include <map>
#include <cstring>
#include <algorithm>

int main() {
    char s[101];
    scanf ("%s", s);
    
    int length = strlen(s);
    // printf ("%d\n", length);
    
    if (length == 1) {
        printf ("1\n");
        return 0;
    }
    
    char front[101];
    char back[101];
    
    int p = 0;
    
    if (length % 2 == 0) {
        int half = int(length / 2);
        
        for (int i = 0; i < half; i++) {
            front[i] = s[i];
        }
        
        for (int j = length-1; j >= half; j--) {
            back[p++] = s[j];
        }
    }
    
    else {
        int half = int(length / 2);
        // printf ("%d\n", half);
        
        for (int i = 0; i < half; i++) {
            front[i] = s[i];
        }
        
        for (int j = length-1; j > half; j--) {
            back[p++] = s[j];
        }
    }
    
    front[p] = '\0';
    back[p] = '\0';
    
    // printf ("%s %s\n", front, back);
    
    if (strcmp(front, back) == 0) {
        printf ("1\n");
    }
        
    else {
        printf ("0\n");
    }
    
    return 0;
}
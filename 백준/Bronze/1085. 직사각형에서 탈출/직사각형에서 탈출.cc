#include <cstdio>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>

int main() {
    int x, y, w, h;
    scanf ("%d %d %d %d", &x, &y, &w, &h);
    
    int arr[] = {x, y, h-y, w-x};
    
    // for (int i = 0; i < 4; i++) {
    //     printf ("%d ", arr[i]);
    // } printf ("\n");
    
    int min = std::min({abs(x), abs(y), abs(h-y), abs(w-x)});
    
    printf ("%d", min);
    
    return 0;
}
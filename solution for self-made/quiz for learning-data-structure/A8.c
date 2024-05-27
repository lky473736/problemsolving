#include <stdio.h>
#include <stdbool.h>

int arr[] = {3, 2, 4, 1, 5};
void print(int n);

int main() {
    int temp;
    
    print (0);
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4 - i; j++) {
            if (arr[j] < arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
        
        print (i+1);
    }

    return 0;
}

void print (int n) {
    printf ("pass %d : ", n);
    
    for (int i = 0; i < 5; i++) {
        printf ("%5d", arr[i]);
    }
    
    printf ("\n");
}

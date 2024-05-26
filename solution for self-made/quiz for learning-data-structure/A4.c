#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int circular_queue[5] = {};
int head = 0, tail = 0;
int n = 5;

int push (int val) {
    tail = (tail+1) % n;
    
    if (head == tail) {
        if (circular_queue[tail] == 0) {
            circular_queue[tail] = val;
            return 0;
        }
        
        else {
            return -1;
        }
    }
    
    else {
        circular_queue[tail] = val;
    }
}

int pop () {
    head = (head+1) % n;
    
    if (head == tail && circular_queue[tail] == 0) {
        return -1;
    }
    
    else {
        circular_queue[head] = 0;
    }
}

void print () {
    printf ("current state : ");
    
    for (int i = 0; i < n; i++) {
        printf ("%d ", circular_queue[i]);
    }
    
    printf ("\n");
}

int main() {
    printf ("append the value\n");
    for (int i = 0; i < n; i++) {
        push(i+1);
        print();
    }
    
    printf ("\n");
    printf ("delete the value\n");
    for (int i = 0; i < n; i++) {
        pop();
        print();
    }
    
    return 0;
}

// stack을 사용하여 풀이

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAX_STACK_SIZE 100

typedef struct {
    int data[MAX_STACK_SIZE];
    int top;
} Stack;

void push (Stack *s, int value) {
    s->data[++(s->top)] = value;
}

int pop (Stack *s) {
    return s->data[(s->top)--];
}

int evaluate_postfix (const char *expression) {
    Stack s = {.top = -1};
    const char *token = expression;

    while (*token) {
        if (isdigit(*token)) {
            int num = 0;
            
            while (isdigit(*token)) {
                num = num * 10 + (*token - '0');
                token++;
            }
            
            push(&s, num);
        } 
        
        else if (*token == ' ') {
            token++;
        } 
        
        else {
            int b = pop(&s);
            int a = pop(&s);
            
            switch (*token) {
                case '+': push(&s, a + b); break;
                case '-': push(&s, a - b); break;
                case '*': push(&s, a * b); break;
                case '/': push(&s, a / b); break;
            }
            
            token++;
        }
    }
    
    return pop(&s);
}

int main() {
    const char expression[] = "3 10 2 * + 4 -";
    printf ("result: %d\n", evaluate_postfix(expression));
    
    return 0;
}

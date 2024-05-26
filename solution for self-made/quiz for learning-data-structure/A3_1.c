// stack을 사용하지 않고 풀이

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int is_operator (int *arr, int n, int k) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == k) {
            return 1;
        }
    }
    
    return 0;
}

int main()
{
    /*
        embedding
        
        + -> -1
        - -> -2
        * -> -3
        / -> -4
    */
    
    int postfix_formula[7] = {3, 10, 2, -3, -1, 4, -2}; // 3 10 2 * + 4 -
    int operators[4] = {-1, -2, -3, -4};
    
    while (true) {
        // operand, operand, operator
        
        int box[3] = {0, 0, 0};
        int j = 0;
        int k = 0;
        int position_initial[3] = {0, 0, 0};

g1 : 
        for (int i = k; i < 7; i++) {
            printf ("%d ", postfix_formula[i]);
            if (postfix_formula[i] != 0 && j < 3) {
                box[j] = postfix_formula[i];
                position_initial[j] = i;
                
                j++;
            }
            
            if (j == 3) {
                int condition1 = !is_operator(operators, 4, box[0]) && !is_operator(operators, 4, box[1]);
                int condition2 = is_operator(operators, 4, box[2]);
                
                if (condition1 && condition2) {
                    break;
                }
                
                else {
                    k++;
                    j = 0;
                    goto g1;
                }
            }
        }
        
        printf (" || ");
        
        for (int i = 0; i < 3; i++){
            printf ("(%d, %d) ", position_initial[i], box[i]);
        }
        
        printf ("\n");
        
        if (j == 1) {
            printf ("result : %d", box[0]);
            break;
        }
        
        else {
            switch (box[2]) {
                case -1 : postfix_formula[position_initial[2]] = box[0] + box[1]; break;
                case -2 : postfix_formula[position_initial[2]] = box[0] - box[1]; break;
                case -3 : postfix_formula[position_initial[2]] = box[0] * box[1]; break;
                case -4 : postfix_formula[position_initial[2]] = box[0] / box[1]; break;
            }
                
            postfix_formula[position_initial[0]] = 0;
            postfix_formula[position_initial[1]] = 0;
        }
    }
    
    return 0;
}

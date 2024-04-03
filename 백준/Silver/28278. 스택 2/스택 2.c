#include <stdio.h>
#include <string.h>

int arr[1000001];
int counting = 0;

void push(int X) {
    arr[counting] = X;
    counting += 1;
}

void pop() {
    if (counting == 0) {
        printf ("-1\n");
    }
    
    else {
        printf ("%d\n", arr[counting-1]);
        arr[counting] = 0;
        counting -= 1;
    }
}

// void size() {
//     printf ("%d\n", counting);
// }

void empty() {
    if (counting == 0) {
        printf ("1\n");
    }
    
    else {
        printf ("0\n");
    }
}

// void top() {
//     if (counting == 0) {
//         printf ("-1\n");
//     }
    
//     else {
//         printf ("%d\n", arr[counting-1]);
//     }
// }

int main() {
    int N;
    scanf ("%d", &N);
    
    for (int i = 0; i < N; i++) {
        int mode;
        scanf ("%d", &mode);
        
        if (mode == 2) {
            pop();
        }
        
        else if (mode == 3) {
            printf ("%d\n", counting);
        }
        
        else if (mode == 4) {
            if (counting == 0) {
				printf("%d\n", 1);
			}
			
			else {
				printf ("%d\n", 0);
			}
        }
        
        else if (mode == 5) {
            if (counting == 0) {
                printf ("-1\n");
            }
                
            else {
                printf ("%d\n", arr[counting-1]);
            }
        }
        
        // else {
        //     std::string num = s.substr(4, s.size());
        //     std::cout << num << std::endl;
            
        //     int inum = std::stoi(num);
        //     printf ("%d\n", inum);
        //     push(inum);
        // }
        
        else {
            int num;
            scanf ("%d", &num);
            push(num);
        }
        
    //     switch (s) {
    //         case "pop" :
    //             pop();
    //             break;
                
    //         case "size" :
    //             size();
    //             break;
                
    //         case "empty" :
    //             empty();
    //             break;
                
    //         case "top" :
    //             top();
    //             break;
                
    //         default : 
    //             std::string num = s.substr(5);
    //             num = std::stoi(num);
    //             push(num);
    //     }
    // }
    }
    
    return 0;
}
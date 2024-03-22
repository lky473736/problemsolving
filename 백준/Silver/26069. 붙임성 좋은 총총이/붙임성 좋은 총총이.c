#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main() 
{
    int N;
    char infectors[1000][21];
    int rainbowmode = 0;
    
    scanf ("%d", &N);
    
    int infector = 0;
    int is_ChongChong = 0; // 총총이가 infectors안에 있는가

    for (int i = 0; i < N; i++) {
        char a[21];
        char b[21];
        scanf ("%s %s", a, b);
        
        if (rainbowmode == 0) {
            if (strcmp(a, "ChongChong") == 0 && strcmp(b, "ChongChong") == 0) { // 둘 다 총총이일 때
                if (is_ChongChong == 0) {
                    strcpy(infectors[infector], "ChongChong");
                    infector += 1;
                    is_ChongChong = 1;
                }
                
                else {
                    ;
                }
            }
            
            else if (strcmp(a, "ChongChong") == 0 && strcmp(b, "ChongChong") != 0) // a가 총총이일 때
            {
                strcpy(infectors[infector], "ChongChong");
                infector += 1;
                strcpy(infectors[infector], b);
                infector += 1;
                is_ChongChong = 1;
                rainbowmode = 1;
            }
            
            else if (strcmp(a, "ChongChong") != 0 && strcmp(b, "ChongChong") == 0) // b가 총총이일 때
            {
                strcpy(infectors[infector], "ChongChong");
                infector += 1;
                strcpy(infectors[infector], a);
                infector += 1;
                is_ChongChong = 1;
                rainbowmode = 1;
            }
            
            else { // 둘 다 아닐 때
                ;
            }
        }
        
        else { // rainbowmode가 작동될 때
            // 찾기
            // printf ("--------\n");
            // printf ("%s %s %d\n", a, b, infector);
            
            // for (int j = 0; j < infector; j++) {
            //     printf ("%s ", infectors[j]);
            // }
            // printf ("\n");
            
            int i_a = 0; // a가 infectors 안에 있는 지 토큰
            int i_b = 0; // b가 infectors 안에 있는 지 토큰
            
            // printf ("a\n");
            for (int j = 0; j < infector; j++) { // a
                // printf ("%s %s\n", infectors[j], a);
                if (strcmp(infectors[j], a) == 0) {
                    i_a = 1;
                    break;
                }
            }
            
            // printf ("b\n");
            for (int j = 0; j < infector; j++) { // b
                // printf ("%s %s\n", infectors[j], b);
                if (strcmp(infectors[j], b) == 0) {
                    i_b = 1;
                    break;
                }
            }
            
            if (i_a == 1 && i_b == 1) { // 둘 다 infectors 안에 있다면
                ;
            }
            
            else if (i_a == 1 && i_b == 0) { // i_a가 infectors 안에 있다면
                strcpy(infectors[infector], b);
                infector += 1;
            }
            
            else if (i_a == 0 && i_b == 1) { // i_b가 infectors 안에 있다면
                strcpy(infectors[infector], a);
                infector += 1;
            }
            
            else { // 둘 다 infectors 안에 없다면
                ;
            }
        }
    }
    
    //     int temp_t = 0;
        
    //     if (rainbowmode == 1) {
    //         for (int j = 0; j < infector; j++) {
    //             // if (strcmp(a, logp[j]) == 0 || strcmp(b, logp[j]) == 0) {
    //             //     printf ("trigger\n");
    //             //     if (strcmp(a, logp[j]) == 0 && strcmp(b, logp[j]) == 0) {
    //             //         break;
    //             //     }
    //             //     else {
    //             //         infector += 1;
                        
    //             //         if (strcmp(a, logp[j]) == 0)
    //             //         {
    //             //             strcpy(logp[infector], b);
    //             //         }
                        
    //             //         else if (strcmp(b, logp[j]) == 0) {
    //             //             // logp[infector] = b;
    //             //             strcpy(logp[infector], a);
    //             //         }
                        
    //             //         break;
    //             //     }
    //             // }
                
    //             if (strcmp(a, "ChongChong") != 0 && strcmp(b, "ChongChong") != 0)
    //             {
    //                 if (strcmp(a, logp[j]) == 0 && strcmp(b, logp[j]) != 0) {
    //                     strcpy(logp[infector], b);
    //                     infector += 1;
    //                     break;
    //                 } 
                    
    //                 else if (strcmp(b, logp[j]) == 0 && strcmp(a, logp[j]) != 0) {
    //                     strcpy(logp[infector], a);
    //                     infector += 1;
    //                     break;
    //                 }
    //             }
                
    //             else {
    //                 if (strcmp(a, "ChongChong") == 0 && strcmp(b, "ChongChong") != 0) {
    //                     for (int n = 0; n < infector; n++) {
    //                         if (strcmp(b, logp[infector]) == 0) {
    //                             temp_t = 1;
    //                             break;
    //                         }
    //                     }
                        
    //                     if (temp_t == 1) {
    //                         ;
    //                     }
                        
    //                     else {
    //                         infector++;
    //                         strcpy(logp[infector], b);
    //                     }
    //                 }
                    
    //                 else if (strcmp(b, "ChongChong") == 0 && strcmp(a, "ChongChong") != 0) {
    //                     for (int n = 0; n < infector; n++) {
    //                         if (strcmp(a, logp[infector]) == 0) {
    //                             temp_t = 1;
    //                             break;
    //                         }
    //                     }
                        
    //                     if (temp_t == 1) {
    //                         ;
    //                     }
                        
    //                     else {
    //                         infector++;
    //                         strcpy(logp[infector], a);
    //                     }
    //                 }
    //             }
    //         }
    //     }
        
    //     else {
    //         if (strcmp(a, "ChongChong") == 0 && strcmp(b, "ChongChong") == 0) {
    //             ;
    //         }
            
    //         else if (strcmp(a, "ChongChong") == 0 || strcmp(b, "ChongChong") == 0) {
    //             rainbowmode = 1;
    //             strcpy(logp[infector], a);
    //             infector += 1;
    //             strcpy(logp[infector], b);
    //             infector += 1;
    //         }
    //     }
    // }
    
    printf ("%d\n", infector);
    
    // printf ("-----\n");
    
    // for (int p = 0; p < 20; p++) {
    //     printf ("%s\n", infectors[p]);
    // }
        
    
    return 0;
}
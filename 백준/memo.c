#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int main() 
{
    int N;
    char logp[1000][21];
    int rainbowmode = 0;
    
    scanf ("%d", &N);
    
    int infector = 0;

    for (int i = 0; i < N; i++) {
        char a[21];
        char b[21];
        scanf ("%s %s", a, b);
        
        int temp_t = 0;
        
        if (rainbowmode == 1) {
            for (int j = 0; j < infector; j++) {
                // if (strcmp(a, logp[j]) == 0 || strcmp(b, logp[j]) == 0) {
                //     printf ("trigger\n");
                //     if (strcmp(a, logp[j]) == 0 && strcmp(b, logp[j]) == 0) {
                //         break;
                //     }
                //     else {
                //         infector += 1;
                        
                //         if (strcmp(a, logp[j]) == 0)
                //         {
                //             strcpy(logp[infector], b);
                //         }
                        
                //         else if (strcmp(b, logp[j]) == 0) {
                //             // logp[infector] = b;
                //             strcpy(logp[infector], a);
                //         }
                        
                //         break;
                //     }
                // }
                
                if (strcmp(a, "ChongChong") != 0 && strcmp(b, "ChongChong"))
                {
                    if (strcmp(a, logp[j]) == 0 && strcmp(b, logp[j]) != 0) {
                        strcpy(logp[infector], b);
                        infector += 1;
                        break;
                    } 
                    
                    else if (strcmp(b, logp[j]) == 0 && strcmp(a, logp[j]) != 0) {
                        strcpy(logp[infector], a);
                        infector += 1;
                        break;
                    }
                }
                
                else {
                    if (strcmp(a, "ChongChong") == 0 && strcmp(b, "ChongChong") != 0) {
                        for (int n = 0; n < infector; n++) {
                            if (strcmp(b, logp[infector]) == 0) {
                                temp_t = 1;
                                break;
                            }
                        }
                        
                        if (temp_t == 1) {
                            ;
                        }
                        
                        else {
                            infector++;
                            strcpy(logp[infector], b);
                        }
                    }
                    
                    else if (strcmp(b, "ChongChong") == 0 && strcmp(a, "ChongChong") != 0) {
                        for (int n = 0; n < infector; n++) {
                            if (strcmp(a, logp[infector]) == 0) {
                                temp_t = 1;
                                break;
                            }
                        }
                        
                        if (temp_t == 1) {
                            ;
                        }
                        
                        else {
                            infector++;
                            strcpy(logp[infector], a);
                        }
                    }
                }
            }
        }
        
        else {
            if (strcmp(a, "ChongChong") == 0 && strcmp(b, "ChongChong") == 0) {
                ;
            }
            
            else if (strcmp(a, "ChongChong") == 0 || strcmp(b, "ChongChong") == 0) {
                rainbowmode = 1;
                strcpy(logp[infector], a);
                infector += 1;
                strcpy(logp[infector], b);
                infector += 1;
            }
        }
    }
    
    printf ("%d\n", infector);
    
    return 0;
}

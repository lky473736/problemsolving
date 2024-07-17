// #include <bits/stdc++.h>
// using namespace std;

// int arr1[8];
// int arr2[8];
// int arr3[8];
// int arr4[8];
// int *arr_list[4] = {arr1, arr2, arr3, arr4};

// void rotate_posi(int *arr) {
//     int temp = arr[7];
    
//     for (int i = 7; i > 0; i--) {
//         arr[i] = arr[i-1];
//     }
    
//     arr[0] = temp;
// }

// void rotate_nega(int *arr) {
//     int temp = arr[0];
    
//     for (int i = 0; i < 7; i++) {
//         arr[i] = arr[i+1];
//     }
    
//     arr[7] = temp;
// }

// int main() {
//     for (int i = 0; i < 4; i++) {
//         for (int j = 0; j < 8; j++) {
//             char c;
//             cin >> c;
//             arr_list[i][j] = c - '0';
//         }
//     }
    
//     // for (int i = 0; i < 4; i++) {
//     //     for (int j = 0; j < 8; j++) {
//     //         cout << arr_list[i][j];
//     //     }
//     // }
    
//     int K = 0;
//     cin >> K;
    
//     for (int i = 0; i < K; i++) {
//         int nth, direction;
//         cin >> nth >> direction;
        
//         switch (nth) {
//             case 1 :
//                 if (direction == -1) { 
//                     if (arr1[3-1] != arr2[7-1]) {
//                         if (arr2[3-1] != arr3[7-1]) {
//                             if (arr3[3-1] != arr4[7-1]) {
//                                 rotate_posi(arr4);
//                             }
                            
//                             rotate_nega(arr3);
//                         }
                        
//                         rotate_posi(arr2);
//                     }
                    
//                     rotate_nega(arr1);
//                 }
                
//                 else {
//                     if (arr1[3-1] != arr2[7-1]) {
//                         if (arr2[3-1] != arr3[7-1]) {
//                             if (arr3[3-1] != arr4[7-1]) {
//                                 rotate_nega(arr4);
//                             }
                            
//                             rotate_posi(arr3);
//                         }
                        
//                         rotate_nega(arr2);
//                     }
                    
//                     rotate_posi(arr1);
//                 }
//                 break;
            
//             case 2 : 
//                 if (direction == -1) { 
//                     if (arr2[7-1] != arr1[3-1]) {
//                         if (arr2[3-1] != arr3[7-1]) {
//                             if (arr3[3-1] != arr4[7-1]) {
//                                 rotate_posi(arr4);
//                             }
                            
//                             rotate_nega(arr3);
//                         }
                        
//                         rotate_posi(arr1);
//                     }
                    
//                     rotate_nega(arr2);
//                 }
                
//                 else {
//                     if (arr2[7-1] != arr1[3-1]) {
//                         if (arr2[3-1] != arr3[7-1]) {
//                             if (arr3[3-1] != arr4[7-1]) {
//                                 rotate_nega(arr4);
//                             }
                            
//                             rotate_posi(arr3);
//                         }
                        
//                         rotate_nega(arr1);
//                     }
                    
//                     rotate_posi(arr2);
//                 }
//                 break;
            
//             case 3 :
//                 if (direction == -1) { 
//                     if (arr3[7-1] != arr2[3-1]) {
//                         if (arr2[7-1] != arr1[3-1]) {
//                             if (arr3[3-1] != arr4[7-1]) {
//                                 rotate_posi(arr4);
//                             }
                            
//                             rotate_nega(arr1);
//                         }
                        
//                         rotate_posi(arr2);
//                     }
                    
//                     rotate_nega(arr3);
//                 }
                
//                 else {
//                     if (arr3[7-1] != arr2[3-1]) {
//                         if (arr2[7-1] != arr1[3-1]) {
//                             if (arr3[3-1] != arr4[7-1]) {
//                                 rotate_nega(arr4);
//                             }
                            
//                             rotate_posi(arr1);
//                         }
                        
//                         rotate_nega(arr2);
//                     }
                    
//                     rotate_posi(arr3);
//                 }
//                 break;
            
//             case 4 : 
//                 if (direction == -1) { 
//                     if (arr4[7-1] != arr3[3-1]) {
//                         if (arr3[7-1] != arr2[3-1]) {
//                             if (arr2[7-1] != arr1[3-1]) {
//                                 rotate_posi(arr1);
//                             }
                            
//                             rotate_nega(arr2);
//                         }
                        
//                         rotate_posi(arr3);
//                     }
                    
//                     rotate_nega(arr4);
//                 }
                
//                 else {
//                     if (arr4[7-1] != arr3[3-1]) {
//                         if (arr3[7-1] != arr2[3-1]) {
//                             if (arr2[7-1] != arr1[3-1]) {
//                                 rotate_nega(arr4);
//                             }
                            
//                             rotate_posi(arr1);
//                         }
                        
//                         rotate_nega(arr2);
//                     }
                    
//                     rotate_posi(arr3);
//                 }
//                 break;
            
//             default : 
//                 break;
//         }
//     }
    
//     int score = 0;
//     if (arr1[0] == 1) {
//         score += 1;
//     }
    
//     if (arr2[0] == 1) {
//         score += 2;
//     }
    
//     if (arr3[0] == 1) {
//         score += 4;
//     }
    
//     if (arr4[0] == 1) { 
//         score += 8;
//     }
    
//     cout << score;
    
//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int arr1[8];
int arr2[8];
int arr3[8];
int arr4[8];
int *arr_list[4] = {arr1, arr2, arr3, arr4};

void rotate_posi(int *arr) {
    int temp = arr[7];
    for (int i = 7; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = temp;
}

void rotate_nega(int *arr) {
    int temp = arr[0];
    for (int i = 0; i < 7; i++) {
        arr[i] = arr[i + 1];
    }
    arr[7] = temp;
}

int main() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 8; j++) {
            char c;
            cin >> c;
            arr_list[i][j] = c - '0';
        }
    }
    
    int K;
    cin >> K;
    
    for (int i = 0; i < K; i++) {
        int nth, direction;
        cin >> nth >> direction;
        nth--; 
        
        int rotate_dir[4] = {0};
        rotate_dir[nth] = direction;
        
        for (int j = nth; j < 3; j++) {
            if (arr_list[j][2] != arr_list[j + 1][6]) {
                rotate_dir[j + 1] = -rotate_dir[j];
            } else {
                break;
            }
        }
        
        for (int j = nth; j > 0; j--) {
            if (arr_list[j][6] != arr_list[j - 1][2]) {
                rotate_dir[j - 1] = -rotate_dir[j];
            } else {
                break;
            }
        }

        for (int j = 0; j < 4; j++) {
            if (rotate_dir[j] == 1) {
                rotate_posi(arr_list[j]);
            } else if (rotate_dir[j] == -1) {
                rotate_nega(arr_list[j]);
            }
        }
    }
    
    int score = 0;
    if (arr1[0] == 1) score += 1;
    if (arr2[0] == 1) score += 2;
    if (arr3[0] == 1) score += 4;
    if (arr4[0] == 1) score += 8;
    
    cout << score << endl;
    
    return 0;
}
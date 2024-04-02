#include <cstdio>
#include <iostream> 

int t;
int a, b;
int arr[300];

int main() {
	for (int i = 1; i <= 300; i++)
		arr[i] = arr[i - 1] + i;
		 
	for (scanf("%d", &t); t--;) {
		int groupa = 0, groupb = 0, xa, ya, xb, yb;

		scanf("%d %d", &a, &b);

		for (int i = 0; i < 143; i++) {
			if (arr[i] < a && a <= arr[i + 1])
				groupa = i+1;
				
			if (arr[i] < b && b <= arr[i + 1])
				groupb = i + 1;
				
			if (groupa && groupb) break;
		}
		
		xa = a - arr[groupa - 1];
		ya = groupa + 1 - xa;
		
		xb = b - arr[groupb - 1];
		yb = groupb + 1 - xb;

		int x = xa + xb, y = ya + yb;
		int group = x + y - 1;
		printf("%d\n", arr[group - 1] + x);
	}
	
	return 0;
}

// #include <cstdio>
// #include <iostream>
// #include <map>
// #include <cstring>
// #include <algorithm>
// #include <cmath>
// #include <vector>

// // 1) 둘 중에 최댓값 catch
// // 2) 최댓값만큼 map 생성
// // 3) map 생성해서 위치 구해지면
// // 4) 그 위치까지의 counting 출력

// std::map<int, std::vector<int>> creator (int endcount);
// int finder(int px, int py);


// int main() {
//     int T;
//     scanf ("%d", &T);
    
//     for (int i = 0; i < T; i++) {
//         int x, y;
//         scanf ("%d %d", &x, &y);
        
//         int max = x > y ? x : y;
        
//         std::map<int, std::vector<int>> dots = creator(max);
        
//         std::vector<int> position = {1, 1};
//         // int keys[10000];
        
//         std::vector<int> position_x = dots[x-1];
//         std::vector<int> position_y = dots[y-1];
        
//         int x_val, y_val;
//         x_val = position_x[0] + position_y[0];
//         y_val = position_x[1] + position_y[1];
        
//         int rst = finder (x_val, y_val);
//         printf ("%d\n", rst+1);
//     }
    
//     return 0;
// }

// std::map<int, std::vector<int>> creator (int endcount) {
//     std::map<int, std::vector<int>> dots;
//     int counting = 0;
//     std::vector<int> position = {1, 1};
    
//     while (true) {
//         if (counting > endcount) {
//             break;
//         }
        
//         else {
//             // keys[counting] = counting;
//             dots[counting] = std::vector<int>(position);
            
//             if (position[1] == 1) {
//                 position[1] = position[0]+1;
//                 position[0] = 1;
//                 // position = {1, position[0]+1};
//             }
            
//             else {
//                 int temp1 = position[0];
//                 int temp2 = position[1];
                
//                 position[0] = temp1+1;
//                 position[1] = temp2-1;
//             }
//         }
        
//         counting += 1;
//     }
    
//     return (dots);
// }

// int finder(int px, int py) {
//     std::map<int, std::vector<int>> dots;
//     int counting = 0;
//     std::vector<int> position = {1, 1};
    
//     while (true) {
//         if (position[0] == px && position[1] == py) {
//             break;
//         }
        
//         else {
//             // keys[counting] = counting;
//             dots[counting] = std::vector<int>(position);
            
//             if (position[1] == 1) {
//                 position[1] = position[0]+1;
//                 position[0] = 1;
//                 // position = {1, position[0]+1};
//             }
            
//             else {
//                 int temp1 = position[0];
//                 int temp2 = position[1];
                
//                 position[0] = temp1+1;
//                 position[1] = temp2-1;
//             }
//         }
        
//         counting += 1;
//     }
    
//     return (counting);
// }
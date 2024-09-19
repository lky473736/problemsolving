// import java.io.BufferedReader;
// import java.io.BufferedWriter;
// import java.io.IOException;
// import java.io.InputStreamReader;
// import java.io.OutputStreamWriter;
// import java.util.HashMap;

// public class Main {
//     int calculate (int[] arr) {
//         int rst = 0;
        
//         for (int i = 3; i > 0; i--) {
//             if (arr[i] != 0) {
//                 rst += Math.pow(2, i);
//             }
//         }
        
//         return rst;
//     }
    
//     public static void main(String[] args) throws IOException {
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//         BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

//         var inputs = br.readLine();
//         var length = inputs.length();
        
//         var idx = length - 1;
//         long cnt = length / 3;
        
//         List<Number> list = new ArrayList<>(); 
        
//         if (cnt != 0) {
//             while (true) {
//                 int[] arr = new int[3];
                
//                 idx -= 3;
                
//                 if (idx == -3) {
//                     break; 
//                 }
                
//                 else if (idx == -2) {
//                     arr[2] = inputs[idx];
//                     break;
//                 }
                
//                 else if (idx == -1) {
//                     arr[1] = inputs[idx + 1];
//                     arr[2] = inputs[idx + 2];
//                     break;
//                 }
                
//                 else {
//                     arr[0] = inputs[idx];
//                     arr[1] = inputs[idx + 1];
//                     arr[2] = inputs[idx + 2];
//                 }
                
//                 list.add(calculate(arr));
//             }
//         }
        
//         else { 
//             int[] arr = new int[3];
            
//             if (length == 2) {
//                 arr[1] = inputs[0];
//                 arr[2] = inputs[1];
//             }
            
//             if (length == 1) {
//                 arr[2] = inputs[0];
//             }
            
//             list.add(calculate(arr)); 
//         }
        
//         for (int i = arr.size()-1; i >= 0; i--) {
//             bw.write(list[i]);
//         }
        
//         bw.flush();
//     }
// }

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {
    int calculate(int[] arr) {
        int rst = 0;
        
        for (int i = 2; i >= 0; i--) { 
            if (arr[i] != 0) {
                rst += Math.pow(2, 2 - i);
            }
        }
        
        return rst;
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String inputs = br.readLine();
        int length = inputs.length();
        
        int idx = length;
        int cnt = length / 3;  
        
        Main main = new Main();
        List<Integer> list = new ArrayList<>(); 
        
        if (cnt != 0) {
            while (true) {
                int[] arr = new int[3];
                
                idx -= 3;
                
                if (idx == -3) {
                    break;
                } 
                
                else if (idx == -1) {
                    arr[1] = inputs.charAt(0) - '0';
                    arr[2] = inputs.charAt(1) - '0';
                    list.add(main.calculate(arr));
                    break;
                } 
                
                else if (idx == -2) {
                    arr[2] = inputs.charAt(0) - '0';
                    list.add(main.calculate(arr));
                    break;
                } 
                
                else {
                    arr[0] = inputs.charAt(idx) - '0';
                    arr[1] = inputs.charAt(idx + 1) - '0';
                    arr[2] = inputs.charAt(idx + 2) - '0';
                    list.add(main.calculate(arr));
                }
            }
        } 
        
        else { 
            int[] arr = new int[3];
            
            if (length == 2) {
                arr[1] = inputs.charAt(0) - '0';
                arr[2] = inputs.charAt(1) - '0';
            } 
            
            else if (length == 1) {
                arr[2] = inputs.charAt(0) - '0';
            }
            
            list.add(main.calculate(arr)); 
        }
        
        for (int i = list.size() - 1; i >= 0; i--) {
            bw.write(Integer.toString(list.get(i)));
        }
        
        bw.flush();
    }
}
// // import java.util.Scanner;
// // import java.util.ArrayList;

// // public class Main {
// //     public static void main(String[] args) {
// //         Main main = new Main();
// //         Scanner input = new Scanner(System.in);

// //         int money = input.nextInt();
// //         int BNP = 0, TIMING = 0;
// //         int arr[] = new int[15];
// //         int token = -1;
        
// //         int moneyBNP = money;
// //         int moneyTIMING = money;
        
// //         for (int i = 1; i <= 14; i++) {
// //             int compo = input.nextInt();
// //             arr[i] = compo;
            
// //             if (i >= 3) {
// //                 if (arr[i-2] < arr[i-1] && arr[i-1] < arr[i] ) {
// //                     token = 1; // 매도
// //                 }
                
// //                 if (arr[i-2] > arr[i-1] && arr[i-1] > arr[i] ) {
// //                     token = 2; // 매수
// //                 }
                
// //                 if (arr[i-2] == arr[i-1] || arr[i-1] == arr[i]) {
// //                     token = -1;
// //                 }
// //             }
            
// //             if (token == -1) {
// //                 ;
// //             }
            
// //             else if (token == 2) {
// //                 TIMING += moneyTIMING / arr[i];
// //                 moneyTIMING = moneyTIMING % arr[i];
// //             }
            
// //             else {
// //                 moneyTIMING = moneyTIMING + TIMING * arr[i];
// //                 TIMING = 0;
// //             }
            
// //             if (moneyBNP > arr[i]) {
// //                 BNP += moneyBNP / arr[i];
// //                 moneyBNP = moneyBNP % arr[i];
// //             }
// //         }
        
// //         int totalBNP = BNP * arr[14] + moneyBNP;
// //         int totalTIMING = TIMING * arr[14] + moneyTIMING;
        
// //         if (totalBNP > totalTIMING) {
// //             System.out.println("BNP");
// //         }
        
// //         if (totalBNP < totalTIMING) {
// //             System.out.println("TIMING");
// //         }
        
// //         if (totalBNP == totalTIMING) {
// //             System.out.println("SAMESAME");
// //         }

// //         input.close();
// //     }
// // }

// import java.util.Scanner;

// public class Main {
//     public static void main(String[] args) {
//         Main main = new Main();
//         Scanner input = new Scanner(System.in);

//         int money = input.nextInt();
//         int BNP = 0, TIMING = 0;
//         int arr[] = new int[15];
//         int token = -1;
        
//         int moneyBNP = money;
//         int moneyTIMING = money;
        
//         for (int i = 1; i <= 14; i++) {
//             int compo = input.nextInt();
//             arr[i] = compo;
            
//             if (i >= 3) {
//                 if (arr[i-2] < arr[i-1] && arr[i-1] < arr[i]) {
//                     token = 1;
//                 }

//                 if (arr[i-2] > arr[i-1] && arr[i-1] > arr[i]) {
//                     token = 2;
//                 }

//                 if (arr[i-2] == arr[i-1] || arr[i-1] == arr[i]) {
//                     token = -1;
//                 }
//             }

//             if (token == -1) {
//                 ;
//             }

//             else if (token == 2) {
//                 TIMING += moneyTIMING / arr[i];
//                 moneyTIMING = moneyTIMING % arr[i];
//             }

//             else {
//                 moneyTIMING = moneyTIMING + TIMING * arr[i];
//                 TIMING = 0;
//             }

//             if (moneyBNP > arr[i]) {
//                 BNP += moneyBNP / arr[i];
//                 moneyBNP = moneyBNP % arr[i];
//             }
//         }
        
//         int totalBNP = BNP * arr[14] + moneyBNP;
//         int totalTIMING = TIMING * arr[14] + moneyTIMING;
        
//         if (totalBNP > totalTIMING) {
//             System.out.println("BNP");
//         }

//         if (totalBNP < totalTIMING) {
//             System.out.println("TIMING");
//         }

//         if (totalBNP == totalTIMING) {
//             System.out.println("SAMESAME");
//         }

//         input.close();
//     }
// }

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int money = input.nextInt(); // 초기 자금
        int[] prices = new int[14]; // 14일간의 주가

        // 주가 입력 받기
        for (int i = 0; i < 14; i++) {
            prices[i] = input.nextInt();
        }

        // BNP 전략
        int moneyBNP = money;
        int stockBNP = 0;
        for (int i = 0; i < 14; i++) {
            // 살 수 있는 주식 최대 매수
            stockBNP += moneyBNP / prices[i];
            moneyBNP %= prices[i];
        }
        int totalBNP = moneyBNP + stockBNP * prices[13]; // 14일 자산

        // TIMING 전략
        int moneyTIMING = money;
        int stockTIMING = 0;
        for (int i = 3; i < 14; i++) {
            // 3일 연속 상승 시 전량 매도
            if (prices[i - 3] < prices[i - 2] && prices[i - 2] < prices[i - 1] && prices[i - 1] < prices[i]) {
                moneyTIMING += stockTIMING * prices[i]; // 모든 주식 매도
                stockTIMING = 0;
            }
            // 3일 연속 하락 시 전량 매수
            else if (prices[i - 3] > prices[i - 2] && prices[i - 2] > prices[i - 1] && prices[i - 1] > prices[i]) {
                stockTIMING += moneyTIMING / prices[i]; // 가능한 만큼 주식 매수
                moneyTIMING %= prices[i];
            }
        }
        int totalTIMING = moneyTIMING + stockTIMING * prices[13]; // 14일 자산

        // 결과 비교
        if (totalBNP > totalTIMING) {
            System.out.println("BNP");
        } else if (totalBNP < totalTIMING) {
            System.out.println("TIMING");
        } else {
            System.out.println("SAMESAME");
        }

        input.close();
    }
}
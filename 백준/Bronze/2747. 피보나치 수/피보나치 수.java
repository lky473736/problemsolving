// import java.util.*;

// public class Main {
// 	public static void main(String[] args) {
// 	    Scanner scan = new Scanner(System.in);
// 	    int n = scan.nextInt();
	    
// 	    if (n == 1) {
// 	        System.out.println(0);
// 	    }
	    
// 	    else if (n == 2) {
// 	        System.out.println(1);
// 	    }
	    
// 	    else if (n == 3) {
// 	        System.out.println(1);
// 	    }
	    
// 	    else {
//     	    int a = 0, b = 1;
    	    
//     	    for (int i = 0; i < n-1; i++) {
//     	        int temp = b; 
//     	        b = a + b;
//     	        a = temp;
//     	    }
    	   
//     	    System.out.println(b); 
// 	    }
// 	}
// }
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        System.out.println(recur(n));
    }

    public static int recur(int n){
        int[] arr = new int[46];
        arr[0] = 0;
        arr[1] = 1;
        arr[2] = 1;

        for (int i = 3; i < arr.length; i++) {
            arr[i] = arr[i-2] + arr[i-1];
        }

        return arr[n];
    }
}
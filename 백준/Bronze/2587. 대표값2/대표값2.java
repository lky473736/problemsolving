import java.util.*;

public class Main {
	public static void main(String[] args) {
	    Scanner scan = new Scanner(System.in);
	    int suma = 0;
	    int[] arr = new int[5];
	    for (int i = 0; i < 5; i++) {
	        arr[i] = scan.nextInt();
	        suma += arr[i];
	    }
	    
	    System.out.println(suma/5);
	    Arrays.sort(arr);
	    System.out.println(arr[2]); 
	}
}

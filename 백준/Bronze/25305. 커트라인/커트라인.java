import java.util.*;

public class Main {
	public static void main(String[] args) {
	    Scanner scan = new Scanner(System.in);
	    int N = scan.nextInt();
	    int k = scan.nextInt();
	    int[] arr = new int[N];
	    for (int i = 0; i < N; i++) {
	        arr[i] = scan.nextInt();
	    }
	    
	    Arrays.sort(arr);
	    System.out.println(arr[N-k]);
	}
}

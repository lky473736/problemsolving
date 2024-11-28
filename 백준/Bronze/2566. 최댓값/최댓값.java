import java.util.*;

public class Main {
	public static void main(String[] args) {
	    Scanner scan = new Scanner(System.in);
	    
	    int[][] arr = new int[9][9];
	    int max = -1, x = 0, y = 0;
	    for (int i = 0; i < 9; i++) {
	        for (int j = 0; j < 9; j++) {
	            arr[i][j] = scan.nextInt();
	            if (arr[i][j] >= max) {
	                x = i+1; 
	                y = j+1;
	                max = arr[i][j];
	            }
	        }
	    }
	    
	    System.out.printf("%d\n%d %d", max, x, y);
	}
}

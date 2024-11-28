import java.util.*;

public class Main {
	public static void main(String[] args) {
	    Scanner scan = new Scanner(System.in);
	    String input = scan.next();
	    char[] s = input.toCharArray();

	    int token = 0;
	    if (s.length % 2 == 0) {
	        for (int i = 0; i < s.length/2; i++) {
	            if (s[i] != s[s.length-1-i]) {
	                token = 1;
	            }
	        }
	    }
	    else {
	        for (int i = 0; i < s.length/2-1; i++) {
	            if (s[i] != s[s.length-1-i]) {
	                token = 1;
	            }
	        }
	    }
	    
	    if (token == 0) {
	        System.out.println(1);
	    }
	    else {
	        System.out.println(0);
	    }
	}
}

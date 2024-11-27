import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt(); 
        
        int i = 1;
        
        while (i <= N) {
            for (int j = 0; j < i; j++) {
                System.out.printf ("*");
            }
            System.out.println();
            i++;
        }
    }
}

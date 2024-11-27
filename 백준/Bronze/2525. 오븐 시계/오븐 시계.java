import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int A = scan.nextInt();
        int B = scan.nextInt();
        int min = scan.nextInt();
        
        B += min;
        if (B >= 60) {
            A += B / 60;
            B = B % 60;
            if (A >= 24) {
                A %= 24;
            }
        }
        
        System.out.printf ("%d %d", A, B); 
    }
}

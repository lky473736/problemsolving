import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt();
        int i = 1;
        
        do {
            System.out.printf ("%d * %d = %d\n", N, i, N * i++);
        } while (i <= 9);
    }
}

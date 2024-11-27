import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt(); 
        int tmp = N-1;
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < i; j++) {
                System.out.printf(" ");
            }
            for (int j = 0; j < 2*tmp+1; j++) {
                System.out.printf("*");
            }
            System.out.println();
            tmp--;
        }
    }
}

import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int S1 = scan.nextInt();
        int S2 = scan.nextInt();
        
        int token_1 = 0, token_2 = 0;
        for (int i = 0; i < S1; i++) {
            long l1 = scan.nextLong();
            long l2 = scan.nextLong();
            if (l1 != l2) {
                token_1 = 1;
                break;
            }
        }
        for (int i = 0; i < S2; i++) {
            long l1 = scan.nextLong();
            long l2 = scan.nextLong();
            if (l1 != l2) {
                token_2 = 1;
                break;
            }
        }
        if (token_1 == 1) {
            System.out.println("Wrong Answer");
            System.exit(0); 
        }
        
        else if (token_2 == 1) {
            System.out.println ("Why Wrong!!!");
            System.exit(0); 
        }
        
        System.out.println("Accepted");
    }
}
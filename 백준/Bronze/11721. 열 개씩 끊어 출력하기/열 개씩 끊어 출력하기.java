import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        String word = scan.next();
        
        for (int i = 1; i <= word.length(); i++) {
            System.out.printf("%c", word.charAt(i-1));
            if (i % 10 == 0) {
                System.out.println();
            }
        }
    }
}

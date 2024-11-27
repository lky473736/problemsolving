import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        String word = scan.next();
        int suma = 0; 

        for (int i = 0; i < N; i++) {
            suma += Integer.parseInt(String.valueOf(word.charAt(i)));
        }
        System.out.println(suma);
    }
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt(); 
        int min = 1000001;
        int max = -1000001;
        
        for (int i = 0; i < N; i++) {
            int compo = scan.nextInt();
            if (compo <= min) {
                min = compo;
            }
            if (compo >= max) {
                max = compo;
            }
        }
        
        System.out.printf ("%d %d", min, max);
    }
}

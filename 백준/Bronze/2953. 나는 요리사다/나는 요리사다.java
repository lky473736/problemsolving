import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int max = -1;
        int pl = 0;
        
        for (int i = 0; i < 5; i++) {
            int suma = 0;
            for (int j = 0; j < 4; j++) {
                suma += scan.nextInt(); 
            }
            
            if (suma >= max) {
                max = suma;
                pl = i+1;
            }
        }
        
        System.out.printf ("%d %d", pl, max);
    }
}

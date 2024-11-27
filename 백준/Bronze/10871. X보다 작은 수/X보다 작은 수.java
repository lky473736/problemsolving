import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt(); 
        int X = scan.nextInt();
        
        int[] arr = new int[N];
        int j = 0;
        
        for (int i = 0; i < N; i++) {
            int compo = scan.nextInt();
            if (compo < X) {
                arr[j] = compo;
                j++;
            }
        }
        
        for (int i = 0; i < j; i++) {
            System.out.printf ("%d ", arr[i]);
        }
    }
}

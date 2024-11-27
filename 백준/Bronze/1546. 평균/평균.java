import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        int[] arr = new int[N];
        double suma = 0;
        int max = -1;
        for (int i = 0; i < N; i++) {
            arr[i] = scan.nextInt();
            if (max <= arr[i]) {
                max = arr[i];
            }
        }
        for (int i = 0; i < N; i++) {
            suma += ((double)arr[i]/max) * 100;
        }
        
        
        System.out.println(suma/N);
    }
}

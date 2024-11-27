import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N, M;
        N = scan.nextInt();
        M = scan.nextInt();
        
        int[][] mat1 = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                mat1[i][j] = scan.nextInt();
            }
        }
        
        int K = scan.nextInt();
        for (int i = 0; i < K; i++) {
            int x1, y1, x2, y2;
            x1 = scan.nextInt();
            y1 = scan.nextInt();
            x2 = scan.nextInt();
            y2 = scan.nextInt();
            
            int suma = 0;
            for (int j = x1-1; j <= x2-1; j++) {
                for (int k = y1-1; k <= y2-1; k++) {
                    suma += mat1[j][k];
                }
            }
            System.out.println(suma);
        }
    }
}

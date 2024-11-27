import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int N, M;
        N = scan.nextInt();
        M = scan.nextInt();
        
        int[][] mat1 = new int[N][M];
        int[][] mat2 = new int[N][M];
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                mat1[i][j] = scan.nextInt();
            }
        }
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                mat2[i][j] = scan.nextInt();
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                mat1[i][j] += mat2[i][j];
            }
        }
        
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.printf("%d ", mat1[i][j]);
            }
            System.out.println();
        }
    }
}

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        Scanner input = new Scanner(System.in); 
        
        int n = input.nextInt();
        
        for (int i = 1; i <= 2*n-1; i++) {
            for (int j = 0; j < Math.abs(n-i); j++) {
                System.out.print(' ');
            }
            
            for (int j = 1; j <= n-Math.abs(n-i); j++) {
                System.out.print('*');
            }
            
            System.out.println();
        }
    }
}
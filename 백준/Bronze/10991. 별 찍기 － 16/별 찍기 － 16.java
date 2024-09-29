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
        int p = n-1;
        
        for (int i = 1; i <= n; i++) {
            for (int j = p; j > 0; j--) {
                System.out.print(' ');
            }
            
            p--;
            
            System.out.print('*');
            
            if (i >= 2) {
                int k = 2*(i-1) -1;
                for (int j = 0; j < k; j++) {
                    if (j % 2 == 0) {
                        System.out.print(' ');
                    }
                    
                    else {
                        System.out.print('*');
                    }
                }
                
                System.out.print('*');
            }
            
            System.out.println();
        }
    }
}
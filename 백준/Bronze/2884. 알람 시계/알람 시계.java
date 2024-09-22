import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        Scanner input = new Scanner(System.in); 
        
        int H = input.nextInt();
        int M = input.nextInt();
        
        if (M >= 45) {
            M -= 45;
        }
        
        else {
            if (H != 0) {
                H -= 1;
                M += 15;
            }
            
            else {
                H = 23;
                M += 15;
            }
        }
        
        System.out.println(H + " " + M);
    }
}
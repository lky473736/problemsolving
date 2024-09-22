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
        
        while (true) {
            int a = input.nextInt();
            int b = input.nextInt();
            
            if (a == 0 && b == 0) {
                break;
            }
            
            else {
                if (b % a == 0) {
                    System.out.println("factor");
                }
                
                else if (a % b == 0) {
                    System.out.println("multiple");
                }
                
                else {
                    System.out.println("neither");
                }
            }
        }
    }
}
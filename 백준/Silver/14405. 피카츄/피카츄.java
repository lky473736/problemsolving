import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        Scanner input = new Scanner(System.in); 
        
        String S = input.next();
        int currentInd = 0;
        int token = 0;
        
        while (currentInd < S.length()) {
            if (currentInd + 2 <= S.length() && S.substring(currentInd, currentInd+2).equals("pi")) {
                currentInd += 2;
                continue;
            }
            
            if (currentInd + 2 <= S.length() && S.substring(currentInd, currentInd+2).equals("ka")) {
                currentInd += 2;
                continue;
            }
            
            if (currentInd + 3 <= S.length() && S.substring(currentInd, currentInd+3).equals("chu")) {
                currentInd += 3;
                continue;
            }
            
            token = 1; 
            break;  
        }
        
        if (token == 1) {
            System.out.println("NO");
        } 
        
        else {
            System.out.println("YES");
        }
    }
}

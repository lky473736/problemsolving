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
        
        int N = input.nextInt();
        
        String prev = "";
        for (int i = 0; i < N; i++) {
            String compo = input.next();
            
            if (i == 0) {
                prev = compo;
            }
            
            else {
                StringBuilder sb = new StringBuilder(prev);
                
                for (int j = 0; j < compo.length(); j++) {
                    if (prev.charAt(j) == compo.charAt(j)) {
                        ;
                    }
                    
                    else {
                        sb.setCharAt(j, '?');
                    }
                }
                
                prev = sb.toString();
            }
        }
        
        System.out.println(prev);
    }
}
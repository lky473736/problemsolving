import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        Scanner input = new Scanner(System.in); 
        
        while (true) {
            String compo = input.next();
            
            if (compo.equals("end")) {
                break;
            }
            
            int rule1 = 0;
            int rule2 = 1;
            int rule3 = 1;
            
            HashSet<String> set = new HashSet<>(Arrays.asList("a", "e", "i", "o", "u"));

            for (int i = 0; i < compo.length(); i++) {
                if (set.contains(String.valueOf(compo.charAt(i)))) {
                    rule1 = 1;
                }
                
                if (i > 0) {
                    if ((compo.charAt(i-1) == 'e' && compo.charAt(i) == 'e') || 
                        (compo.charAt(i-1) == 'o' && compo.charAt(i) == 'o')) {
                        // Allow 'ee' or 'oo'
                    } else if (compo.charAt(i-1) == compo.charAt(i)) {
                        rule3 = 0;
                        break;
                    }
                    
                    if (i >= 2) {
                        if (set.contains(String.valueOf(compo.charAt(i-2))) &&
                            set.contains(String.valueOf(compo.charAt(i-1))) &&
                            set.contains(String.valueOf(compo.charAt(i)))) {
                            rule2 = 0;
                            break;
                        }
                        
                        if (!set.contains(String.valueOf(compo.charAt(i-2))) && 
                            !set.contains(String.valueOf(compo.charAt(i-1))) && 
                            !set.contains(String.valueOf(compo.charAt(i)))) {
                            rule2 = 0;
                            break;
                        }
                    }
                }
            }
            
            if (rule1 + rule2 + rule3 == 3) {
                System.out.println('<' + compo + '>' + " is acceptable.");
            } else {
                System.out.println('<' + compo + '>' + " is not acceptable.");
            }
        }
    }
}
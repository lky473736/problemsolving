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
        
        int A = input.nextInt();
        String B = input.next();
        
        long compo1 = A * Integer.parseInt(String.valueOf(B.charAt(2)));
        long compo2 = A * Integer.parseInt(String.valueOf(B.charAt(1))); 
        long compo3 = A * Integer.parseInt(String.valueOf(B.charAt(0)));
        
        System.out.println(compo1);
        System.out.println(compo2);
        System.out.println(compo3);
        System.out.println(compo1 + compo2 * 10 + compo3 * 100);
    }
}
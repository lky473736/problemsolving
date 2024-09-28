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
        
        int cnt = 0;
        
        for (int i = 0; i < 5; i++) {
            int compo = input.nextInt();
            if (n == compo) {
                cnt++;
            }
        }
        
        System.out.println(cnt);
    }
}
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
        
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < 3; i++) {
            int cnt = 0;
            char rst = '0';
            
            for (int j = 0; j < 4; j++) {
                int compo = input.nextInt();
                
                if (compo == 0) {
                    cnt++;
                }
            }
            
            if (cnt == 1) {
                rst = 'A';
            }
            
            else if (cnt == 2) {
                rst = 'B';
            }
            
            else if (cnt == 3) {
                rst = 'C';
            }
            
            else if (cnt == 4) {
                rst = 'D';
            }
            
            else {
                rst = 'E';
            }
            
            System.out.println(rst);
        }
    }
}
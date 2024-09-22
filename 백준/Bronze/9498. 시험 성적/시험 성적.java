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
        
        int score = input.nextInt();
        char rst = '0';
        
        if (score >= 90) {
            rst = 'A'; 
        }
        
        if (rst == '0' && score >= 80) {
            rst = 'B'; 
        }
        
        if (rst == '0' && score >= 70) {
            rst = 'C'; 
        }
        
        if (rst == '0' && score >= 60) {
            rst = 'D'; 
        }
        
        if (rst == '0') {
            rst = 'F';
        }
        
        System.out.println(rst);
    }
}
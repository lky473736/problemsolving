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

        for (int i = 0; i < 4; i++) {
            int compo = input.nextInt();
            
            if (i == 2) {
                list.add(Math.abs(compo-list.get(0)));
            }
            
            else if (i == 3) {
                list.add(Math.abs(compo-list.get(1)));
            }
            
            else {
                list.add(compo);
            }
        }
        
        Collections.sort(list);
        System.out.println(list.get(0));
    }
}
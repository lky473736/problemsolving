import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        
        int T = scanner.nextInt();
        scanner.nextLine();
        
        while (T-- != 0) {
            int N = scanner.nextInt();
            scanner.nextLine();
            
            String line = scanner.nextLine();  
            String[] inputs = line.split(" ");
            
            int sumation = 0;
            for (String input : inputs) {
                sumation += Integer.parseInt(input);  
            }
            
            System.out.println(sumation);
        }
        
        scanner.close();
    }
}

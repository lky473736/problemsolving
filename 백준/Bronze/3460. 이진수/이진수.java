import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    ArrayList<Integer> calculateBinary(int num) {
        ArrayList<Integer> binaryCode = new ArrayList<>();
        int rest_num = num;
        
        while (rest_num > 0) {
            binaryCode.add(rest_num % 2);  
            rest_num /= 2;                
        }
        
        return binaryCode;
    }
    
    public static void main(String[] args) {
        Main main = new Main();
        Scanner scanner = new Scanner(System.in);
        
        int T = scanner.nextInt(); 
        
        while (T-- > 0) {
            int n = scanner.nextInt();  
            ArrayList<Integer> binaryCode = main.calculateBinary(n); 
            
            for (int i = 0; i < binaryCode.size(); i++) {
                if (binaryCode.get(i) == 1) { // 하나씩 빼오기 (idx 위치에서)
                    System.out.print(i + " "); 
                }
            }
            
            System.out.println();  // 각 테스트 케이스마다 줄 바꿈
        }
        
        scanner.close();
    }
}
